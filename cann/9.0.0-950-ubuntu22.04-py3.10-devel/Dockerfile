FROM quay.io/ascend/cann:9.0.0-950-ubuntu22.04-py3.10

##############
# User: root #
##############
# Set env
USER root
ENV USER root

# Set bash
RUN echo "dash dash/sh boolean false" | debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash

# Install base tools
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt install -y vim \
    zip \
    tree \
    dos2unix \
    sudo \
    bzip2 \
    pigz \
    locales \
    libgtest-dev \
    pkg-config \
    systemctl \
    gawk \
    nlohmann-json3-dev \
    patch \
    && apt-get clean all
    
# Install googletest
RUN git clone --depth 1 -b release-1.11.0 https://github.com/google/googletest.git /tmp/googletest && \
    cd /tmp/googletest && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    rm -rf /tmp/googletest

# Install python plugin 
RUN mkdir /root/.pip \
    && echo "[global]" > /root/.pip/pip.conf \
    && echo "index-url=https://repo.huaweicloud.com/repository/pypi/simple" >> /root/.pip/pip.conf \
    && echo "trusted-host=repo.huaweicloud.com" >> /root/.pip/pip.conf \
    && echo "timeout=120" >> /root/.pip/pip.conf \
    && pip3 install --upgrade pip && cd /tmp \
    && pip3 install wheel==0.38.4 \
    && pip3 install pyyaml==6.0.1  \
    && pip3 install setuptools==67.4.0  \
    && pip3 install numpy==1.26.4  \
    && pip3 install attrs \
    && pip3 install decorator \
    && pip3 install sympy \
    && pip3 install psutil \
    && pip3 install scipy \
    && pip3 install protobuf

WORKDIR /opt