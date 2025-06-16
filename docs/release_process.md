# Motivation / Problem description

## Original intention
Currently, the Ascend Community official website has only released the Toolkit development kit package, Kernels operator package, NNAL acceleration library package, etc. of CANN in the run, deb, rpm, zip, and tar.gz types. Users need to download and install the software packages on demand, which brings a less relaxed experience. In order to provide users with an out-of-the-box experience, we have created a CANN image based on Ubuntu OS or openEuler OS, Python, and CANN (Toolkit development kit package, Kernels operator package, NNAL acceleration library), and published the image to three mainstream container platforms: AscendHub, DockerHub, and Quay.io, and provided users with a version-matching Dockerfile as a reference.

## User cases
- As a CANN user, I hope to be able to experience the new version of CANN as soon as it is released, and I can also use the updates of CANN quickly;
- As an upstream supporter of the Ascend community, I hope to build new application container images based on CANN images so that developers can quickly experience their use.

## Detailed description of the plan
### Tag Rules
Tag is all lowercase, the format is `<cann-version>-<chip>-<os><os-version>-<py-version>`
- For the alpha version image of CANN, cann-verison example: 8.1.rc1.alpha001
- For the beta version image of CANN, cann-version example: 8.1.rc1 (without beta1)
- For python version, py-version example: py3.11

tag example: 8.1.rc1-910b-openeuler22.03-py3.11

### Special tags
- 8.2.rc1.alpha001
  Indicates an image based on Ubuntu OS with CANN version 8.2.RC1.alpha001

- 8.2.rc1 
  Indicates an image based on Ubuntu OS with CANN version 8.2.RC1.beta1

- latest
  Indicates the latest CANN version image based on Ubuntu OS

## Release process
The release process of cann-container-image is as follows: add CANN new version parameters to build_arg.json, which is used by template.py to generate a new version of the dockerfile file; add CANN new version parameters to publish_version.json and .github/workflows/build_and_push.yml files to manually trigger the CI process of publishing a new tag image.

Currently, CANN container images have been published to DockerHub, Quay.io, and AscendHub repositories. The image access links are as follows:
- https://quay.io/repository/ascend/cann
- https://hub.docker.com/r/ascendai/cann
- https://www.hiascend.com/developer/ascendhub/detail/cann

## Precautions
Following the docker guide, we define CANN's environment variables in the dockerfile using ENV, but the ATB_HOME_PATH environment variable of CANN's NNAL package is determined by `torch.compiled_with_cxx_abi()`. If `torch.compiled_with_cxx_abi()` is true, then `ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0`, otherwise `ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1`.

To meet the user's usage requirements, we define `ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0` and write `source /usr/local/Ascend/nnal/atb/set_env.sh` to bashrc and ENTRYPOINT to ensure that the atb value is set correctly when the user starts the container interactively and non-interactively.

- The effect of using ENTRYPOINT to set environment variables: If the user starts the container through `docker run image bash`, `source set_env.sh` will take effect;
- The effect of writing environment variables to bashrc: If the user starts the container through `docker run -d` and then uses `docker exec -it container bash` to interact with the container, the bashrc file will be read and `source set_env.sh` will take effect.