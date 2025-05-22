# Quick reference

-	**Where to get help**:  
	[Ascend Community](https://www.hiascend.com/forum/)

-	**Where to file issues**:  
	https://github.com/Ascend/cann-container-image/issues

-	**Published image artifact details**:  
    -	the `remote` directory:
        -	gathered from the [AscendHub](https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884)/[DockerHub](https://hub.docker.com/r/ascendai/cann/tags)/[Quay.io](https://quay.io/repository/ascend/cann?tab=tags)

        -	image digests/blobs, transfer sizes, image metadata, etc.

    -	the `local` directory:

        -	inspected from the image on-disk after it is pulled

        -	installed packages, creation date, architecture, environment variables, detected licenses, etc.

# Supported tags and respective `Dockerfile` links
You can find the currently released tags and corresponding dockerfiles in the cann directory of the repository:
<br>
https://github.com/Ascend/cann-container-image/blob/main/cann

# What is CANN?

CANN (Compute Architecture for Neural Networks) is a heterogeneous computing architecture launched by Ascend for AI scenarios. It supports multiple AI frameworks and serves AI processors and programming. It plays a key role in connecting the upper and lower levels and is a key platform for improving the computing efficiency of Ascend AI processors. At the same time, it provides efficient and easy-to-use programming interfaces for diverse application scenarios, supporting users to quickly build AI applications and businesses based on the Ascend platform.

## Online Documentation

You can find the latest CANN documentation, including a programming guide, on the [project web page](https://www.hiascend.com/software/cann). This README file only contains basic setup instructions.

## Usage

Assuming your NPU device is mounted at `/dev/davinci1` and your NPU driver is installed at `/usr/local/Ascend`:

```docker
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
    -it ascendai/cann:latest bash
```

## Build

Run the following command in the root directory:

```docker
docker build \
    -t ascendai/cann:latest \
    -f cann/tag/dockerfile .
```

# License

Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.