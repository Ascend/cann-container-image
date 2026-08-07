# Atlas CANN

> English | [中文](./OVERVIEW.zh.md)

CANN (Compute Architecture for Neural Networks) is a heterogeneous computing architecture launched by Huawei for AI scenarios. It supports multiple AI frameworks on the upper layer and serves AI processors and programming on the lower layer, acting as a key bridge and a key platform for improving the computing efficiency of Atlas AI processors.

---

## Image Download

For the latest CANN images, please go to the [Image Download](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884) page to download them. The latest version is 9.1.0.

---

## Image Categories

### CANN Base Container Images

CANN base images are built on the Ubuntu and openEuler operating systems and include CANN (Toolkit development kit, Ops operator package, and NNAL acceleration library) along with a Python environment.

#### Tag Format

Tags follow this format:

```
<cann-version>-<chip-series>-<os>-<python-version>
```

| Field | Example Values | Description |
|---|---|---|
| `cann-version` | `9.1.0`, `9.0.1`, `9.1.0-beta.3`, `9.0.0`, `8.5.2`, etc. | CANN version number |
| `chip-series` | `950`, `910`, `a3` | Target Atlas chip series |
| `os` | `ubuntu22.04`, `openeuler24.03` | Base operating system |
| `python-version` | `py3.10`, `py3.11`, `py3.12` | Python version |


#### CANN 9.1.0 Base Container Images: Tags & Dockerfile Links
| Tag | Dockerfile | Image Contents |
|-----|------------|----------|
| [`9.1.0-310p-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-310p-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-910-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-910-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-910b-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-910b-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-950-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-950-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-a3-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-ubuntu22.04-py3.12/Dockerfile) | toolkit/ops/nnal |
| [`9.1.0-a3-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-openeuler24.03-py3.12/Dockerfile) | toolkit/ops/nnal |

> Note: On aarch64, the `9.1.0-950-*` images additionally include URMA (Unified RoCE Message Access) for RoCE-based distributed communication; x86_64 images do not include it.


### CANN Development Container Images

CANN Development Container Images are built on top of the base images. In addition to the CANN toolkit suite and Python runtime environment, they come with extra OS utilities (such as zip, vim, tree, etc.), selected Python plugins (such as wheel, pyyaml, setuptools, etc.), and GoogleTest pre-installed, enabling you to quickly perform operator development on top of these images.

#### Tag Format

Tags follow this format:

```
<cann_base_tag>-devel
```

| Field | Example Values | Description |
|---|---|---|
| `cann_base_tag` | `9.1.0-310p-ubuntu22.04-py3.12` | CANN base image tag |


#### CANN 9.1.0 Development Container Images: Tags & Dockerfile Links
| Tag | Dockerfile | Image Contents |
|-----|------------|----------|
| [`9.1.0-310p-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-310p-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-910-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-910-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-910b-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-910b-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-950-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-950-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-a3-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |
| [`9.1.0-a3-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-openeuler24.03-py3.12-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plugin/googletest |

> Note: On aarch64, the `9.1.0-950-*` images additionally include URMA (Unified RoCE Message Access) for RoCE-based distributed communication; x86_64 images do not include it.

---

## Quick Start

### Prerequisites

#### Install Driver

An Atlas NPU driver compatible with the CANN version inside the container must be installed on the host. Please visit the [CANN compatibility site](https://www.hiascend.com/developer/download/compatibility) for the correspondence between driver and CANN versions.

### Run a CANN Container

```bash
export CANN_REPO=swr.cn-south-1.myhuaweicloud.com/ascendhub/cann
export CANN_TAG=9.1.0-a3-ubuntu22.04-py3.12

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
### Run a CANN Container on 950 Series aarch64 Products

```bash
export CANN_REPO=swr.cn-south-1.myhuaweicloud.com/ascendhub/cann
export CANN_TAG=9.1.0-950-openeuler24.03-py3.12

docker run \
    --name cann_container \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/hisi_hdc \
    --device /dev/ummu \
    --device /dev/uburma \
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
export CANN_TAG=9.1.0-a3-ubuntu22.04-py3.12
# need to install buildx
docker buildx build -t $CANN_REPO:$CANN_TAG -f cann/$CANN_TAG/Dockerfile .
```

---

## Supported Hardware

| Chip Series | Product Examples | Architecture |
|---|---|---|
| Atlas 950 | Atlas 950PR, Atlas 950DT | ARM64 / x86_64 |
| Atlas 910 | Atlas 800T A2, Atlas 900 A2 PoD，Atlas 800 | ARM64 / x86_64 |
| Atlas A3 | Atlas 800T A3 | ARM64 / x86_64 |

For more hardware support, please visit [Atlas Product Form Descriptions](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)

---

## References

If you want to learn how to download CANN software packages, please visit the [CANN download site](https://www.hiascend.com/cann/download?versionId=769&ids=d806%2Ch0501%2Ch0601%2Ch0702).
If you want to learn more about CANN, including release notes, programming guides, APIs, and development tools, please visit the [CANN documentation site](https://www.hiascend.com/cann/document).

---

## License

View the [license information](https://www.hiascend.com/en/legal/cannua-download?isNewCon=true) for CANN software included in these images.

As with all container images, pre-installed packages (Python, system libraries, etc.) may be subject to their own licenses.
