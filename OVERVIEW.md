# Atlas CANN

> English | [中文](./OVERVIEW.zh.md)

CANN (Compute Architecture for Neural Networks) is a heterogeneous computing architecture launched by Huawei for AI scenarios. It supports multiple AI frameworks on the upper layer and serves AI processors and programming on the lower layer, acting as a key bridge and a key platform for improving the computing efficiency of Atlas AI processors.

---

## Image Download

CANN 9.1.0 has been released. Please visit the [Mirror Download](https://quay.io/repository/ascend/cann?tab=tags) page to obtain it.

---

## CANN Base Container Images && CANN Development Container Images

The CANN base images are built on Ubuntu and openEuler operating systems. They include the CANN toolkit (Toolkit development suite, ops operator package, NNAL acceleration library) and the Python environment.

CANN Development Container Images are built on CANN Base Container Images. In addition to the CANN toolkit suite and Python runtime environment, they come with extra OS utilities(such as zip, vim, tree, etc.), selected Python plugins(such as wheel, pyyaml, setuptools, etc.), and GoogleTest pre-installed.

---

## Supported Tags and Dockerfile Links

### Tag Naming Rules

CANN Tags follow this pattern:

```
<cann_version>-<chip_series>-<os>-<python_version>
```

| Field | Example Values | Description |
|---|---|---|
| `cann-version` | `9.1.0`, `9.0.1`, `9.1.0-beta.3`, `9.0.0`, `8.5.2`, etc. | CANN version number |
| `chip-series` | `950`, `a3`, `910b`, `910`, `310p` | Target Atlas chip series |
| `os` | `ubuntu22.04`, `openeuler24.03` | Base operating system |
| `python-version` | `py3.10`, `py3.11`, `py3.12` | Python version |
| `-devel` | `-devel` | Optional suffix, representing a development image |



### LATEST CANN 9.1.0

For tags associated with historical versions, please refer to [Supported Tags](https://github.com/Ascend/cann-container-image/tree/main/supported_tags.md).

| Tag | Dockerfile | content |
|---|---|---|
| [`9.1.0-310p-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-ubuntu22.04-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-310p-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-openeuler24.03-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-910-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-ubuntu22.04-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-910-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-openeuler24.03-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-910b-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-ubuntu22.04-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-910b-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-openeuler24.03-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-950-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-ubuntu22.04-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-950-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-openeuler24.03-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-a3-ubuntu22.04-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-ubuntu22.04-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-ubuntu22.04-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-a3-openeuler24.03-py3.12`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-openeuler24.03-py3.12) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-openeuler24.03-py3.12/Dockerfile) | toolkit, ops, nnal |
| [`9.1.0-310p-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-310p-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-310p-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-310p-openeuler24.03-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-910-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-910-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910-openeuler24.03-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-910b-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-910b-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-910b-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-910b-openeuler24.03-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-950-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-950-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-950-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-950-openeuler24.03-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-a3-ubuntu22.04-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-ubuntu22.04-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-ubuntu22.04-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |
| [`9.1.0-a3-openeuler24.03-py3.12-devel`](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884?version=9.1.0-a3-openeuler24.03-py3.12-devel) | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.1.0-a3-openeuler24.03-py3.12-devel/Dockerfile) | toolkit, ops, nnal, os-tool, Python-plugin, googletest |

> Note: On aarch64, the `9.1.0-950-*` images additionally include URMA (Unified RoCE Message Access) for RoCE-based distributed communication; x86_64 images do not include it.

---

## Quick Start

### Prerequisites

#### Install Driver

An Atlas NPU driver compatible with the CANN version inside the container must be installed on the host. Please visit the [CANN compatibility site](https://www.hiascend.com/developer/download/compatibility) for the correspondence between driver and CANN versions.

### Run a CANN Container

```bash
export CANN_REPO=quay.io/ascend/cann
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
export CANN_REPO=quay.io/ascend/cann
export CANN_TAG=9.1.0-950-openeuler24.03-py3.12

docker run \
    --name cann_container \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/hisi_hdc \
    --device /dev/ummu \
    --device /dev/uburma \
    -v /dev/log:/dev/log \
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

## References

If you want to learn how to download CANN software packages, please visit the [CANN download site](https://www.hiascend.com/cann/download?versionId=769&ids=d806%2Ch0501%2Ch0601%2Ch0702).
If you want to learn more about CANN, including release notes, programming guides, APIs, and development tools, please visit the [CANN documentation site](https://www.hiascend.com/cann/document).

---

## License

View the [license information](https://www.hiascend.com/en/legal/cannua-download?isNewCon=true) for CANN software included in these images.

As with all container images, pre-installed packages (Python, system libraries, etc.) may be subject to their own licenses.
