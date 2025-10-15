# Stage 1: Install Python
FROM quay.io/pypa/manylinux_2_28:latest AS python-installer

# Python Environment variables
ENV PATH=/usr/local/python3.11.13/bin:${PATH}

RUN yum update -y && \
    yum install -y \
        gcc \
        gcc-c++ \
        make \
        cmake \
        curl \
        zlib-devel \
        bzip2-devel \
        openssl-devel \
        ncurses-devel \
        sqlite-devel \
        readline-devel \
        tk-devel \
        gdbm-devel \
        libpcap-devel \
        xz-devel \
        libev-devel \
        expat-devel \
        libffi-devel \
        systemtap-sdt-devel \
    && yum clean all \
    && rm -rf /var/cache/yum \
    && rm -rf /tmp/*

# Install Python
RUN curl -fsSL https://repo.huaweicloud.com/python/3.11.13/Python-3.11.13.tgz -o /tmp/Python-3.11.13.tgz && \
    tar -xf /tmp/Python-3.11.13.tgz -C /tmp && \
    cd /tmp/Python-3.11.13 && \
    mkdir -p /usr/local/python3.11.13/lib && \
    ./configure --enable-shared --enable-shared LDFLAGS="-Wl,-rpath /usr/local/python3.11.13/lib" --prefix=/usr/local/python3.11.13 && \
    make -j $(nproc) && \
    make altinstall && \
    ln -sf /usr/local/python3.11.13/bin/python3.11 /usr/local/python3.11.13/bin/python3 && \
    ln -sf /usr/local/python3.11.13/bin/pip3.11 /usr/local/python3.11.13/bin/pip3 && \
    ln -sf /usr/local/python3.11.13/bin/python3 /usr/local/python3.11.13/bin/python && \
    ln -sf /usr/local/python3.11.13/bin/pip3 /usr/local/python3.11.13/bin/pip && \
    rm -rf /tmp/*

# Stage 2: Install CANN
FROM python-installer AS cann-installer

ARG TARGETPLATFORM

RUN yum update -y && \
    yum install -y \
        unzip \
        pciutils \
        net-tools \
        lapack-devel \
        gcc-gfortran \
        util-linux \
        findutils \
        wget \
    && yum clean all \
    && rm -rf /var/cache/yum

# Note: Install CANN runtime dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir \
        attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 \
        psutil protobuf==3.20 scipy requests absl-py

# Note: Get the download link according to ARCH and download the installation package
RUN ARCH=$(case "${TARGETPLATFORM}" in \
        "linux/amd64") echo "x86_64" ;; \
        "linux/arm64") echo "aarch64" ;; \
        *) echo "Unsupported TARGETPLATFORM: ${TARGETPLATFORM}" && exit 1 ;; \
    esac) && \
    CANN_TOOLKIT_URL=https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/Milan-ASL/Milan-ASL%20V100R001C23B800TP024/Ascend-cann-toolkit_8.3.RC1.alpha003_linux-${ARCH}.run && \
    CANN_KERNELS_URL=https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/Milan-ASL/Milan-ASL%20V100R001C23B800TP024/Ascend-cann-kernels-310p_8.3.RC1.alpha003_linux-${ARCH}.run && \
    CANN_NNAL_URL=https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/Milan-ASL/Milan-ASL%20V100R001C23B800TP024/Ascend-cann-nnal_8.3.RC1.alpha003_linux-${ARCH}.run && \
    wget --quiet --header="Referer: https://www.hiascend.com/" ${CANN_TOOLKIT_URL} -O ~/Ascend-cann-toolkit.run && \
    wget --quiet --header="Referer: https://www.hiascend.com/" ${CANN_KERNELS_URL} -O ~/Ascend-cann-kernels.run && \
    wget --quiet --header="Referer: https://www.hiascend.com/" ${CANN_NNAL_URL} -O ~/Ascend-cann-nnal.run

# Note: Install CANN Toolkit Development Kit Package
RUN chmod +x ~/Ascend-cann-toolkit.run && \
    ~/Ascend-cann-toolkit.run --quiet --install --install-for-all && \
    rm -f ~/Ascend-cann-toolkit.run

# Note: Install CANN Kernels Operator Package
RUN chmod +x ~/Ascend-cann-kernels.run && \
    ~/Ascend-cann-kernels.run --quiet --install --install-for-all && \
    rm -f ~/Ascend-cann-kernels.run

# Note: Install CANN NNAL Neural Network Acceleration Library
RUN . /usr/local/Ascend/ascend-toolkit/set_env.sh && \
    chmod +x ~/Ascend-cann-nnal.run && \
    ~/Ascend-cann-nnal.run --quiet --install --install-for-all && \
    rm -f ~/Ascend-cann-nnal.run
    
# Stage 3: Copy results from previous stages
FROM quay.io/pypa/manylinux_2_28:latest AS official-manylinux

# Python Environment variables
ENV PATH=/usr/local/python3.11.13/bin:${PATH}

# Note: Toolkit Environment variables, obtained from /usr/local/Ascend/ascend-toolkit/set_env.sh
ENV ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ENV LD_LIBRARY_PATH=/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:$LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH=${ASCEND_TOOLKIT_HOME}/lib64:${ASCEND_TOOLKIT_HOME}/lib64/plugin/opskernel:${ASCEND_TOOLKIT_HOME}/lib64/plugin/nnengine:${ASCEND_TOOLKIT_HOME}/opp/built-in/op_impl/ai_core/tbe/op_tiling:$LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH=${ASCEND_TOOLKIT_HOME}/tools/aml/lib64:${ASCEND_TOOLKIT_HOME}/tools/aml/lib64/plugin:$LD_LIBRARY_PATH
ENV PYTHONPATH=${ASCEND_TOOLKIT_HOME}/python/site-packages:${ASCEND_TOOLKIT_HOME}/opp/built-in/op_impl/ai_core/tbe:$PYTHONPATH
ENV PATH=${ASCEND_TOOLKIT_HOME}/bin:${ASCEND_TOOLKIT_HOME}/compiler/ccec_compiler/bin:${ASCEND_TOOLKIT_HOME}/tools/ccec_compiler/bin:$PATH
ENV ASCEND_AICPU_PATH=${ASCEND_TOOLKIT_HOME}
ENV ASCEND_OPP_PATH=${ASCEND_TOOLKIT_HOME}/opp
ENV TOOLCHAIN_HOME=${ASCEND_TOOLKIT_HOME}/toolkit
ENV ASCEND_HOME_PATH=${ASCEND_TOOLKIT_HOME}

# Note: NNAL Environment variables, obtained from /usr/local/Ascend/nnal/set_env.sh
ENV ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ENV LD_LIBRARY_PATH=${ATB_HOME_PATH}/lib:${ATB_HOME_PATH}/examples:${ATB_HOME_PATH}/tests/atbopstest:${LD_LIBRARY_PATH}
ENV PATH=${ATB_HOME_PATH}/bin:$PATH
ENV ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ENV ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ENV ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ENV ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ENV ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ENV ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ENV ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ENV ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ENV ATB_COMPARE_TILING_EVERY_KERNEL=0
ENV ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ENV ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ENV ATB_SHARE_MEMORY_NAME_SUFFIX=""
ENV ATB_MATMUL_SHUFFLE_K_ENABLE=1
ENV LCCL_DETERMINISTIC=0
ENV LCCL_PARALLEL=0

SHELL [ "/bin/bash", "-c" ]

RUN yum update -y && \
    yum install -y \
        ca-certificates \
        bash \
        glibc \
        sqlite-devel \
        gcc \
        gcc-c++ \
        make \
        cmake \
        git \
        vim \
        wget \
        jq \
        curl \
        build-essential \
        numactl-devel \
    && yum clean all \
    && rm -rf /var/cache/yum \
    && rm -rf /tmp/*

COPY --from=cann-installer /usr/local/python3.11.13 /usr/local/python3.11.13
COPY --from=cann-installer /usr/local/Ascend /usr/local/Ascend
COPY --from=cann-installer /etc/Ascend /etc/Ascend

# Note: Set environment variables
RUN \
    CANN_TOOLKIT_ENV_FILE="/usr/local/Ascend/ascend-toolkit/set_env.sh" && \
    CANN_NNAL_ENV_FILE="/usr/local/Ascend/nnal/atb/set_env.sh" && \
    echo "source ${CANN_TOOLKIT_ENV_FILE}" >> /etc/profile && \
    echo "source ${CANN_TOOLKIT_ENV_FILE}" >> ~/.bashrc && \
    echo "source ${CANN_NNAL_ENV_FILE}" >> /etc/profile && \
    echo "source ${CANN_NNAL_ENV_FILE}" >> ~/.bashrc

ENTRYPOINT ["/bin/bash", "-c", "\
    source /usr/local/Ascend/ascend-toolkit/set_env.sh && \
    source /usr/local/Ascend/nnal/atb/set_env.sh && \
    exec \"$@\"", "--"]
