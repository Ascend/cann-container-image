# 昇腾 CANN 

> [English](./OVERVIEW.md) | 中文

## 快速参考

- CANN 由 [CANN community](https://www.hiascend.com/cann) 维护

- 从哪里获取帮助

    - [AscendHub 镜像仓库](https://ascendhub.huawei.com)
    - [CANN 文档](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition)
    - [昇腾开发者社区](https://www.hiascend.com/developer)
    - [问题反馈](https://github.com/Ascend/cann-container-image/issues)

---

## CANN

CANN（Compute Architecture for Neural Networks，神经网络计算架构）是华为面向 AI 场景推出的异构计算架构。它为昇腾 AI 处理器提供全面的软件栈支持，涵盖算子库、图引擎、运行时库和编译工具链。


---

## 支持的 Tags 及 Dockerfile 链接

### Tag 规范

Tag 遵循以下格式：

```
<cann版本>-<芯片系列>-<操作系统>-<python版本>
```

| 字段 | 示例值 | 说明 |
|---|---|---|
| `cann版本` | `8.5.1`、`8.3.RC2` | CANN 版本号 |
| `芯片系列` | `910`、`910b`、`a3`、`310p` | 目标昇腾芯片系列 |
| `操作系统` | `ubuntu22.04`、`openeuler24.03` | 基础操作系统 |
| `python版本` | `py3.11` | Python 版本 |


### CANN 8.5.1

| Tag | Dockerfile | 镜像内容 |
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

## 快速开始

### 前置要求（可选）

#### 安装驱动

主机上必须安装与容器内 CANN 版本兼容的昇腾 NPU 驱动。请参阅 [CANN 兼容性矩阵](https://www.hiascend.com/document) 了解驱动与 CANN 版本的对应关系。

---

### 运行 CANN 容器

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

### 如何本地构建
```bash
docker buildx build -t {cann_tag} -f {your_repo}/cann/{cann_tag}/Dockerfile .
```

### 如何二次开发
```bash
# 以 CANN 镜像为基础镜像，叠加用户软件
FROM quay.io/ascend/cann:8.5.2-a3-ubuntu22.04-py3.11

RUN apt update -y && \
    apt install gcc ...

...
```

---

## 支持的硬件

| 芯片系列 | 产品示例 | 架构 |
|---|---|---|
| 昇腾 910 | Atlas 800 | ARM64 / x86_64 |
| 昇腾 910B | Atlas 800T A2、Atlas 900 A2 PoD | ARM64 / x86_64 |
| 昇腾 A3 | Atlas 800T A3 | ARM64 / x86_64 |
| 昇腾 310P | Atlas 300I Pro、Atlas 300V Pro | ARM64 / x86_64 |

---

## 许可证

查看这些镜像中包含的 CANN 和 Mind 系列软件的[许可证信息](https://www.hiascend.com/cann)。

与所有容器镜像一样，预装软件包（Python、系统库等）可能受其自身许可证约束。