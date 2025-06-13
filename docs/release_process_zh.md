# 动机 / 问题描述

## 初衷
目前昇腾社区官网只发布了 run、deb、rpm、zip、tar.gz 类型的 CANN 的 Toolkit 开发套件包、Kernels 算子包、NNAL 加速库包等，用户需要按需下载软件包并安装，这带来了不太轻松的体验。为了给用户提供开箱即用的使用体验，我们基于 Ubuntu OS 或 openEuler OS ，Python 和 CANN （ Toolkit 开发套件包、Kernels 算子包、NNAL 加速库）制作了 CANN 镜像，将镜像发布至 AscendHub、DockerHub、Quay.io 三个主流容器平台，并为用户提供版本配套的 Dockerfile 作为参考。

## 用户案例

- 作为 CANN 的使用者，我希望能够在 CANN 版本发布后，第一时间快速体验 CANN 的新版本，同时，CANN 的更新我也能快速使用上；
- 作为昇腾社区的上游支持者，我希望能够基于 CANN 镜像构建新的应用容器镜像，以便开发者可以快速体验使用；

# 方案的详细描述

## 标签规则
tag全小写，格式为 `<cann-version>-<chip>-<os><os-version>-<py-version>`
- 对于 CANN 的 alpha 版本镜像，cann-verison 示例：8.1.rc1.alpha001
- 对于 CANN 的 beta 版本镜像，cann-version 示例：8.1.rc1（不带 beta1 ）
- 对于 python 版本，py-version 示例：py3.11

标签示例：8.1.rc1-910b-openeuler22.03-py3.11

### 特殊标签
- 8.2.rc1.alpha001
  表示基于 Ubuntu OS 的 CANN 版本为 8.2.RC1.alpha001 的镜像

- 8.2.rc1 
  表示基于 Ubuntu OS 的 CANN 版本为 8.2.RC1.beta1 的镜像

- latest
  表示基于 Ubuntu OS 的最新 CANN 版本镜像

## 发布流程
 cann-container-image 的发布流程如下：添加CANN新版本参数至 build_arg.json，用于 template.py 生成新版本的 dockerfile 文件；添加 CANN  新版本参数至 publish_version.json 和 .github/workflows/build_and_push.yml 文件，用于手动触发发布新 tag 镜像的 CI 流程。

目前CANN容器镜像已发布至 DockerHub、Quay.io、AscendHub 仓库，镜像访问链接如下：
- https://quay.io/repository/ascend/cann
- https://hub.docker.com/r/ascendai/cann
- https://www.hiascend.com/developer/ascendhub/detail/cann

## 注意事项

遵循docker指南，我们将 CANN 的环境变量使用 ENV 方式定义在 dockerfile 中，但是 CANN 的 NNAL 包的 ATB_HOME_PATH 环境变量由 `torch.compiled_with_cxx_abi()` 决定，若 `torch.compiled_with_cxx_abi()` 为 true，则 `ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0`，否则 `ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1` 。

为了满足大多数用户的使用要求，我们定义`ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0`，并将`source /usr/local/Ascend/nnal/atb/set_env.sh`写入 bashrc 和 ENTRYPOINT，保证用户使用交互式和非交互式启动容器时 atb 的值设置正确。

- 使用 ENTRYPOINT 设置环境变量的作用：若用户通过 `docker run image bash` 启动容器，`source set_env.sh`会生效；
- 将环境变量写入bashrc的作用：若用户通过`docker run -d`启动容器然后使用`docker exec -it container bash`方式与容器交互，会读取 bashrc 文件，`source set_env.sh`会生效。


