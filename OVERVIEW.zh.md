# 昇腾 CANN 

> [English](./OVERVIEW.md) | 中文

## 快速参考

- CANN 由 [CANN community](https://www.hiascend.com/cann) 维护

- 从哪里获取帮助

    - [AscendHub 镜像仓库](https://www.hiascend.com/developer/ascendhub)
    - [CANN 文档](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition)
    - [昇腾开发者社区](https://www.hiascend.com/developer)
    - [问题反馈](https://github.com/Ascend/cann-container-image/issues)

---

## CANN

CANN（Compute Architecture for Neural Networks，神经网络计算架构）是华为面向 AI 场景推出的异构计算架构。它为昇腾 AI 处理器提供全面的软件栈支持，涵盖算子库、图引擎、运行时库和编译工具链。


---

## 支持的 Tags 及 Dockerfile 链接

### Tag 规范

Tag遵循以下格式：

```
<cann版本>-<芯片系列>-<操作系统>-<python版本>[-devel]
```

| 字段 | 示例值 | 说明 |
|---|---|---|
| `cann版本` | `9.1.0-beta.3`、`9.0.1`、`9.0.0`、`8.5.2` 等 | CANN 版本号 |
| `芯片系列` | `950`、`910`、`910b`、`a3`、`310p` | 目标昇腾芯片系列 |
| `操作系统` | `ubuntu22.04`、`openeuler24.03` | 基础操作系统 |
| `python版本` | `py3.10`、`py3.11`、`py3.12` | Python 版本 |

Tag中包含`-devel`后缀表示开发版CANN镜像，开发版镜像额外安装了部分操作系统工具、Python插件和googletest。

### CANN 9.0.0
#### 以Python3.11为例
| Tag | Dockerfile | 镜像内容 |
|-----|------------|----------|
| `9.0.0-310p-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-310p-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-310p-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-310p-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-910-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-910-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-910b-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910b-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-910b-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910b-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-950-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-950-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-950-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-950-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-a3-ubuntu22.04-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-a3-ubuntu22.04-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-a3-openeuler24.03-py3.11` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-a3-openeuler24.03-py3.11/Dockerfile) | toolkit/ops/nnal |
| `9.0.0-310p-ubuntu22.04-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-310p-ubuntu22.04-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-310p-openeuler24.03-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-310p-openeuler24.03-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-910-ubuntu22.04-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910-ubuntu22.04-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-910-openeuler24.03-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910-openeuler24.03-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-910b-ubuntu22.04-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910b-ubuntu22.04-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-910b-openeuler24.03-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-910b-openeuler24.03-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-950-ubuntu22.04-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-950-ubuntu22.04-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-950-openeuler24.03-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-950-openeuler24.03-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-a3-ubuntu22.04-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-a3-ubuntu22.04-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |
| `9.0.0-a3-openeuler24.03-py3.11-devel` | [Dockerfile](https://github.com/Ascend/cann-container-image/blob/main/cann/9.0.0-a3-openeuler24.03-py3.11-devel/Dockerfile) | toolkit/ops/nnal/os-tool/Python-plug/googletest |

---


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
FROM quay.io/ascend/cann:9.0.0-a3-ubuntu22.04-py3.11

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

查看这些镜像中包含的 CANN 系列软件的[许可证信息](https://www.hiascend.com/legal/cannua-download?isNewCon=true)。

与所有容器镜像一样，预装软件包（Python、系统库等）可能受其自身许可证约束。