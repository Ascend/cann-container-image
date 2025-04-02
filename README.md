# Ascend Docker Images

<p align="center">
    <a href="https://github.com/openmerlin/dockerfile/actions/workflows/docker.yml">
        <img src="https://github.com/openmerlin/dockerfile/actions/workflows/docker.yml/badge.svg" />
    </a>
    <a href="LICENSE">
        <img src="https://img.shields.io/github/license/openmerlin/dockerfile.svg" />
    </a>
    <img src="https://img.shields.io/github/v/release/openmerlin/dockerfile" />
    <img src="https://img.shields.io/badge/language-dockerfile-384D54.svg">
</p>

<p align="center">
    <a href="./README_zh.md">
        <b>中文</b>
    </a> •
    <a href="https://hub.docker.com/u/ascendai">
        <b>Docker Hub</b>
    </a> •
    <a href="https://github.com/orgs/ascend/packages?ecosystem=container">
        <b>GitHub Container</b>
    </a> •
    <a href="https://quay.io/organization/ascend">
        <b>Red Hat Quay</b>
    </a>
</p>

This repository hosts the following Ascend Docker images, providing
base images based on both Ubuntu and OpenEuler. For detailed information,
please refer to the README.md file in each image directory:

- [CANN](./cann)：provides cann-toolkit runtime environment
- [PyTorch](./pytorch): provides torch_npu runtime environment
- [MindSpore](./mindspore): provides MindSpore runtime environment
- [Python](./python): provides a base Python environment

## Usage

Please make sure you have an NPU device and the driver has been installed, then refer to the `docker run` commands
in the image directory's README.md.

## Build

We recommend using [Docker Buildx Bake][1] for building the images. For build
details, see the [docker-bake.hcl](./docker-bake.hcl), and for the build
parameters, check [arg.json](./arg.json).

[1]: https://docs.docker.com/build/bake/

> [!NOTE]
>
> If you don't have Bake, you can find the traditional docker build
> commands in the image directory's README.md.

To build using Bake, Docker Engine 20.10+ is required. Run the following
command in the root directory of this repository:

```docker
docker buildx bake -f arg.json -f docker-bake.hcl
```

To list all targets:

```docker
docker buildx bake -f arg.json -f docker-bake.hcl --print
```

To build single-arch images only:

```docker
docker buildx bake -f arg.json -f docker-bake.hcl \
    --set '*.platform=linux/arm64'
```

> [!NOTE]
>
> - To customize the build configuration, use the `--set`. More details
    here: https://docs.docker.com/reference/cli/docker/buildx/bake/#set
> - To modify build parameters or tag names, edit the [arg.json](./arg.json) file

## Support

The team tracks bugs and enhancement requests using [GitHub issues][2]. Before
submitting a suggestion or bug report, search the existing GitHub issues to
see if your issue has already been reported.

[2]: https://github.com/openmerlin/dockerfile/issues

## License

This repository is licensed under the [Apache License 2.0](./LICENSE).