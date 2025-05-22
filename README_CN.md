## 快速开始
- 官方的 CANN Ascend docker镜像
- 如何获取帮助：[Ascend Community](https://www.hiascend.com/forum/)

## CANN
CANN（Compute Architecture for Neural Networks）是昇腾针对AI场景推出的异构计算架构，对上支持多种AI框架，对下服务AI处理器与编程，发挥承上启下的关键作用，是提升昇腾AI处理器计算效率的关键平台。同时针对多样化应用场景，提供高效易用的编程接口，支持用户快速构建基于昇腾平台的AI应用和业务。<br>
<br>
Ascend-CANN镜像，基于Ubuntu OS或openEuler OS，内部集成系统包、Python和CANN （Toolkit开发套件包、Kernels算子包、NNAL加速库）制作。用户根据实际需要，基于该基础镜像安装人工智能框架，即可运行相应业务程序。

## 支持的tags和相应的Dockerfile链接
每个CANN镜像的tag由CANN版本号和基础镜像版本号组成，具体如下
-	[`8.2.rc1.alpha001-910b-openeuler22.03-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.2.rc1.alpha001-910b-openeuler22.03-py3.10/Dockerfile)
-	[`8.2.rc1.alpha001-910b-ubuntu22.04-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.2.rc1.alpha001-910b-ubuntu22.04-py3.10/Dockerfile)
-	[`8.1.rc1-a3-ubuntu22.04-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.rc1-a3-ubuntu22.04-py3.10/Dockerfile)
-	[`8.1.rc1-a3-openeuler22.03-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.rc1-a3-openeuler22.03-py3.10/Dockerfile)
-	[`8.1.rc1-910b-openeuler22.03-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.rc1-910b-openeuler22.03-py3.10/Dockerfile)
-	[`8.1.rc1-910b-openeuler24.03-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.rc1-910b-openeuler24.03-py3.10/Dockerfile)
-	[`8.1.rc1-910b-ubuntu22.04-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.rc1-910b-ubuntu22.04-py3.10/Dockerfile)
-	[`8.1.RC1.alpha002-910b-openeuler24.03-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.RC1.alpha002-910b-openeuler24.03-py3.10/Dockerfile)
-	[`8.1.RC1.alpha002-910b-ubuntu24.04-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.RC1.alpha002-910b-ubuntu24.04-py3.10/Dockerfile)
-	[`8.1.RC1.alpha001-910b-openeuler22.03-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.RC1.alpha001-910b-openeuler22.03-py3.10/Dockerfile)
-	[`8.1.RC1.alpha001-910b-ubuntu22.04-py3.10`](https://github.com/Ascend/cann-container-image/blob/main/cann/8.1.RC1.alpha001-910b-ubuntu22.04-py3.10/Dockerfile)

## 使用方法

### 快速入门：支持的设备
- Atlas A2训练系列 (Atlas 800T A2, Atlas 900 A2 PoD, Atlas 200T A2 Box16, Atlas 300T A2)
- Atlas 800I A2推理系列 (Atlas 800I A2)

### 快速入门：使用容器设置环境

```bash
# 假设您的NPU设备安装在/dev/davinci1上，并且您的NPU驱动程序安装在/usr/local/Ascend上：
docker run \
    --name cann_container \
    --device /dev/davinci1 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -it ascend/cann:tag bash
```
### 说明：
执行CANN环境变量脚本`/usr/local/Ascend/nnal/atb/set_env.sh`时配置abi参数：<br>
<br>
**自动配置**：执行set_env.sh脚本时，若不加任何参数，且已检测到PyTorch环境时会自动调用`torch.compiled_with_cxx11_abi()`接口，自动选择PyTorch编译时abi参数作为ATB的abi参数，如果没有检测到PyTorch环境则默认配置`abi=1`。<br>
<br>
**手动配置**：执行set_env.sh时，支持用户通过`--cxx_abi=1`和`--cxx_abi=0`参数指定ATB的abi参数。<br>
<br>
在CANN 8.1.RC1及以后版本的镜像中，使用ENV定义ATB的`abi=0`，并将`source /usr/local/Ascend/nnal/atb/set_env.sh`写入bashrc和ENTRYPOINT，确保abi参数的值正确。您也可在容器中手动自行指定ATB的abi参数值。

## 问答
若您没有找到想要的CANN镜像或者在使用镜像时发现任何问题，请随时向我们提出[issue](https://github.com/Ascend/cann-container-image/issues)。


## 许可证
[Apache License, Version 2.0](https://github.com/Ascend/cann-container-image/blob/main/LICENSE)

与所有 Docker 镜像一样，这些镜像可能还包含其他可能受其他许可证约束的软件（例如基础发行版中的 Bash 等，以及所包含主要软件的任何直接或间接依赖项）。

对于任何预构建镜像的使用，镜像用户有责任确保此镜像的任何使用均符合其中包含的所有软件的相关许可证。