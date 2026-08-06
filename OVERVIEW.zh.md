# 昇腾 CANN 

> [English](./OVERVIEW.md) | 中文

CANN（Compute Architecture for Neural Networks）是华为针对 AI 场景推出的异构计算架构，对上支持多种AI框架，对下服务AI处理器与编程，发挥承上启下的关键作用，是提升昇腾 AI 处理器计算效率的关键平台。

---

## 镜像下载
最新 CANN 镜像请前往 [镜像下载](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884) 页面下载。目前最新版本为 9.1.0 。

---

## 镜像分类

### CANN 基础镜像
CANN 基础镜像基于 Ubuntu 和 openEuler 操作系统构建，包含 CANN（Toolkit 开发套件、Ops 算子包、NNAL 加速库）和 Python 环境。

#### Tag 规范

Tag遵循以下格式：

```
<cann版本>-<芯片系列>-<操作系统>-<python版本>
```

| 字段 | 示例值 | 说明 |
|---|---|---|
| `cann版本` | `9.1.0`、`9.0.1`、`9.1.0-beta.3`、`9.0.0`、`8.5.2` 等 | CANN 版本号 |
| `芯片系列` | `950`、`910`、`910b`、`a3`、`310p` | 目标昇腾芯片系列 |
| `操作系统` | `ubuntu22.04`、`openeuler24.03` | 基础操作系统 |
| `python版本` | `py3.10`、`py3.11`、`py3.12` | Python 版本 |


#### CANN 9.1.0 基础镜像 tag 及 Dockerfile 链接
| Tag | Dockerfile | 镜像内容 |
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

> 注：在 aarch64 架构下，`9.1.0-950-*` 镜像额外包含 URMA（Unified RoCE Message Access，统一 RoCE 消息访问）用于 RoCE 分布式通信；x86_64 镜像不包含。


### CANN 开发版镜像

CANN 开发版镜像在基础镜像之上，额外安装了操作系统工具（如 zip、vim、tree 等）、部分 Python 插件（如 wheel、pyyaml、setuptools 等）和 googletest，可基于此镜像快速进行算子开发。

#### Tag 规范

Tag 遵循以下格式：

```
<cann_base_tag>-devel
```

| 字段 | 示例值 | 说明 |
|---|---|---|
| `cann_base_tag` | `9.1.0-310p-ubuntu22.04-py3.12` | CANN基础镜像tag |


#### CANN 9.1.0 开发版镜像tag及Dockerfile链接
| Tag | Dockerfile | 镜像内容 |
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

> 注：在 aarch64 架构下，`9.1.0-950-*` 镜像额外包含 URMA（Unified RoCE Message Access，统一 RoCE 消息访问）用于 RoCE 分布式通信；x86_64 镜像不包含。

---

## 快速开始

### 前置要求

#### 安装驱动

主机上必须安装与容器内 CANN 版本兼容的昇腾 NPU 驱动。请访问 [CANN 版本配套网站](https://www.hiascend.com/developer/download/compatibility)了解驱动与 CANN 版本的对应关系。

### 运行 CANN 容器

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
### 在 950 系列 aarch64 架构产品上运行 CANN 容器

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

### 如何本地构建
```bash
git clone https://github.com/Ascend/cann-container-image.git
cd cann-container-image
export CANN_REPO=my-cann
export CANN_TAG=9.1.0-a3-ubuntu22.04-py3.12
#需安装buildx
docker buildx build -t $CANN_REPO:$CANN_TAG -f cann/$CANN_TAG/Dockerfile .
```

---

## 支持的硬件

| 芯片系列 | 产品示例 | 架构 |
|---|---|---|
| 昇腾 950 | Ascend 950PR、Ascend 950DT |  ARM64 / x86_64  |
| 昇腾 910 | Atlas 800 | ARM64 / x86_64 |
| 昇腾 910B | Atlas 800T A2、Atlas 900 A2 PoD | ARM64 / x86_64 |
| 昇腾 A3 | Atlas 800T A3 | ARM64 / x86_64 |
| 昇腾 310P | Atlas 300I Pro、Atlas 300V Pro | ARM64 / x86_64 |

更多硬件支持请访问[昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)

---

## 参考

若您想了解 CANN 软件包下载方式，请访问 [CANN 下载网站](https://www.hiascend.com/cann/download?versionId=769&ids=d806%2Ch0501%2Ch0601%2Ch0702)。
若您想了解更多关于 CANN 的信息，包括发布说明、编程指南、API 和开发工具，请访问 [CANN 资料网站](https://www.hiascend.com/cann/document)。

---

## 许可证

查看这些镜像中包含的 CANN 系列软件的[许可证信息](https://www.hiascend.com/legal/cannua-download?isNewCon=true)。

与所有容器镜像一样，预装软件包（Python、系统库等）可能受其自身许可证约束。