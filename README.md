## Quick reference
- The offical Ascend CANN docker images
- Where to get help: [Ascend Community](https://www.hiascend.com/forum/)

## CANN
CANN (Compute Architecture for Neural Networks) is a heterogeneous computing architecture launched by Ascend for AI scenarios. It supports multiple AI frameworks and serves AI processors and programming. It plays a key role in connecting the upper and lower levels and is a key platform for improving the computing efficiency of Ascend AI processors. At the same time, it provides efficient and easy-to-use programming interfaces for diverse application scenarios, supporting users to quickly build AI applications and businesses based on the Ascend platform.<br>
<br>
Ascend-CANN image is based on Ubuntu OS or openEuler OS, and integrates system packages, Python and CANN (Toolkit development kit package, Kernels operator package, NNAL acceleration library). Users can install the artificial intelligence framework based on this basic image according to actual needs and run the corresponding business programs.

## Supported tags and respective Dockerfile links
The tag of each Ascend CANN docker image is consist of the version of CANN and the version of basic image. The details are as follows

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

## Usage

### Quick start 1: supported devices
- Atlas A2 Training series (Atlas 800T A2, Atlas 900 A2 PoD, Atlas 200T A2 Box16, Atlas 300T A2)
- Atlas 800I A2 Inference series (Atlas 800I A2)

### Quick start 2: setup environment using container

```bash
# Assuming your NPU device is mounted at /dev/davinci1 and your NPU driver is installed at /usr/local/Ascend:
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

### Note:
Configure the abi parameter when executing the CANN environment variable script `/usr/local/Ascend/nnal/atb/set_env.sh`:<br>
<br>
**Automatic configuration**: When executing the set_env.sh script, if no parameters are added and the PyTorch environment has been detected, the `torch.compiled_with_cxx11_abi()` interface will be automatically called to automatically select the abi parameter when PyTorch is compiled as the abi parameter of ATB. If the PyTorch environment is not detected, abi=1 is configured by default.<br>
<br>
**Manual configuration**: When executing `set_env.sh`, users are supported to specify the abi parameter of ATB through the `--cxx_abi=1` and `--cxx_abi=0` parameters.<br>
<br>
In CANN 8.1.RC1 and later versions of the image, use ENV to define ATB's `abi=0`, and write `source /usr/local/Ascend/nnal/atb/set_env.sh` to bashrc and ENTRYPOINT to ensure that the value of the abi parameter is set correctly when starting the container. You can also manually specify the abi parameter value of ATB in the container.

## Question and answering
If you don't find the CANN image you want or find any problems when using the image, please feel free to file an [issue](https://github.com/Ascend/cann-container-image/issues).

## License
[Apache License, Version 2.0](https://github.com/Ascend/cann-container-image/blob/main/LICENSE)

As with all Docker images, these images may also contain other software that may be subject to other licenses (such as Bash in the base distribution, and any direct or indirect dependencies of the included main software).

For any use of the pre-built image, it is the image user's responsibility to ensure that any use of this image complies with the relevant licenses of all software contained in it.