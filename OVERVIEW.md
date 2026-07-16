# Atlas CANN

> English | [中文](./OVERVIEW.zh.md)

CANN (Compute Architecture for Neural Networks) is a heterogeneous computing architecture launched by Huawei for AI scenarios. It provides comprehensive software stack support for Atlas AI processors, covering operator libraries, graph engines, runtime libraries, and compilation toolchains.

## Quick Reference

- CANN is maintained by the [CANN community](https://www.hiascend.com/cann)

- Where to get help

    - [AtlasHub Image Repository](https://www.hiascend.com/developer/ascendhub)
    - [CANN Documentation](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition)
    - [Atlas Developer Community](https://www.hiascend.com/developer)
    - [Issue Tracker](https://github.com/Ascend/cann-container-image/issues)

---

## CANN Base Container Images

CANN Base Container Images are built on Ubuntu and openEuler operating systems, pre-installed with the CANN toolkit suite, operator (ops) packages, NNAL communication packages, and a Python runtime environment.

### Tag Format

Tags follow this format:

```
<cann-version>-<chip-series>-<os>-<python-version>
```

| Field | Example Values | Description |
|---|---|---|
| `cann-version` | `9.0.1`、`9.1.0-beta.3`、`9.0.0`、`8.5.2` | CANN version number |
| `chip-series` | `910`, `a3`, `310p` | Target Atlas chip series |
| `os` | `ubuntu22.04`, `openeuler24.03` | Base operating system |
| `python-version` | `py3.10`, `py3.11`, `py3.12`  | Python version |


### CANN 9.0.1 Base Container Images: Tags & Dockerfile Links
| Tag | Dockerfile | Image Contents |
|-----|------------|----------|
| `9.0.1-310p-ubuntu22.04-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-310p-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-310p-openeuler24.03-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-310p-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-910-ubuntu22.04-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-910-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-910-openeuler24.03-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-910-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-950-ubuntu22.04-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-950-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-950-openeuler24.03-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-950-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-a3-ubuntu22.04-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-a3-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| `9.0.1-a3-openeuler24.03-py3.12` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-a3-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |

---
## CANN Development Container Images

CANN Development Container Images are built on CANN Base Container Images. In addition to the CANN toolkit suite and Python runtime environment, they come with extra OS utilities(such as zip, vim, tree, etc.), selected Python plugins(such as wheel, pyyaml, setuptools, etc.), and GoogleTest pre-installed.

### CANN 9.0.1 Development Container Images: Tags & Dockerfile Links
| Tag | Dockerfile | Image Contents |
|-----|------------|----------|
| `9.0.1-310p-ubuntu22.04-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-310p-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-310p-openeuler24.03-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-310p-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-910-ubuntu22.04-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-910-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-910-openeuler24.03-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-910-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-950-ubuntu22.04-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-950-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-950-openeuler24.03-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-950-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-a3-ubuntu22.04-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-a3-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| `9.0.1-a3-openeuler24.03-py3.12-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.1-a3-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |

---

## Quick Start

### Prerequisites

#### Install Driver

An Atlas NPU driver compatible with the CANN version inside the container must be installed on the host. Refer to the [CANN Compatibility Matrix](https://www.hiascend.com/document) for driver and CANN version correspondence.

---

### Run a CANN Container

```bash
export CANN_REPO=quay.io/ascend/cann
export CANN_TAG=9.0.1-a3-ubuntu22.04-py3.12

docker run \
    --name cann_container \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -it $CANN_REPO:$CANN_TAG bash
```

### How to Build Locally
```bash
git clone https://github.com/Ascend/cann-container-image.git
cd cann-container-image
export CANN_REPO=my-cann
export CANN_TAG=9.0.1-a3-ubuntu22.04-py3.12
#need install buildx
docker buildx build -t $CANN_REPO:$CANN_TAG -f cann/$CANN_TAG/Dockerfile .
```

---

## Supported Hardware

| Chip Series | Product Examples | Architecture |
|---|---|---|
| Atlas 910 | Atlas 800T A2, Atlas 900 A2 PoD | ARM64 / x86_64 |
| Atlas A3 | Atlas 800T A3 | ARM64 / x86_64 |
| Atlas 310P | Atlas 300I Pro, Atlas 300V Pro | ARM64 / x86_64 |

---

## License

View the [license information](https://www.hiascend.com/legal/cannua-download?isNewCon=true) for CANN software included in these images.

As with all container images, pre-installed packages (Python, system libraries, etc.) may be subject to their own licenses.
