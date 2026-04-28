# Ascend CANN

> English | [中文](./OVERVIEW.zh.md)

## Quick Reference

- CANN is maintained by the [CANN community](https://www.hiascend.com/cann)

- Where to get help

    - [AscendHub Image Repository](https://ascendhub.huawei.com)
    - [CANN Documentation](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition)
    - [Ascend Developer Community](https://www.hiascend.com/developer)
    - [Issue Tracker](https://github.com/Ascend/cann-container-image/issues)

---

## CANN

CANN (Compute Architecture for Neural Networks) is a heterogeneous computing architecture launched by Huawei for AI scenarios. It provides comprehensive software stack support for Ascend AI processors, covering operator libraries, graph engines, runtime libraries, and compilation toolchains.

---

## Supported Tags and Dockerfile Links

### Tag Format

Tags follow this format:

```
<cann-version>-<chip-series>-<os>-<python-version>
```

| Field | Example Values | Description |
|---|---|---|
| `cann-version` | `8.5.1`, `8.3.RC2` | CANN version number |
| `chip-series` | `910`, `910b`, `a3`, `310p` | Target Ascend chip series |
| `os` | `ubuntu22.04`, `openeuler24.03` | Base operating system |
| `python-version` | `py3.11` | Python version |


### CANN 8.5.1

| Tag | Dockerfile | Image Contents |
|---|---|----|
| `8.5.2-a3-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-a3-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-a3-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-a3-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-910b-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-910b-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-910b-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-910b-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-910-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-910-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-910-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-910-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-a3-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-a3-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `8.5.2-a3-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/8.5.2-a3-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |

---

## Quick Start

### Prerequisites (Optional)

#### Install Driver

An Ascend NPU driver compatible with the CANN version inside the container must be installed on the host. Refer to the [CANN Compatibility Matrix](https://www.hiascend.com/document) for driver and CANN version correspondence.

---

### Run a CANN Container

```bash
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
    -it {cann_tag}:latest bash
```

### How to Build Locally
```bash
docker buildx build -t {cann_tag} -f {your_repo}/cann/{cann_tag}/Dockerfile .
```

### How to Extend the Image
```bash
# Use the CANN image as the base image and add your own software on top
FROM quay.io/ascend/cann:8.5.2-a3-ubuntu22.04-py3.11

RUN apt update -y && \
    apt install gcc ...

...
```

---

## Supported Hardware

| Chip Series | Product Examples | Architecture |
|---|---|---|
| Ascend 910 | Atlas 800 | ARM64 / x86_64 |
| Ascend 910B | Atlas 800T A2, Atlas 900 A2 PoD | ARM64 / x86_64 |
| Ascend A3 | Atlas 800T A3 | ARM64 / x86_64 |
| Ascend 310P | Atlas 300I Pro, Atlas 300V Pro | ARM64 / x86_64 |

---

## License

View the [license information](https://www.hiascend.com/cann) for CANN and Mind series software included in these images.

As with all container images, pre-installed packages (Python, system libraries, etc.) may be subject to their own licenses.
