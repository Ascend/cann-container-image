# The rules for publishing CANN container images

## Background
Currently, the [Ascend Community](https://www.hiascend.com/developer/download/community/result) releases CANN Toolkit development suite, Kernels operator packages, and NNAL acceleration library packages in multiple formats (e.g., `.run`, `.deb`, `.rpm`, `.zip`, `.tar.gz`). Users spend significant time downloading and installing appropriate software packages, resulting in a cumbersome experience. 

To enhance user experience, this project aims to build container images based on Ubuntu and openEuler operating systems containing Python and CANN (Toolkit development suite, Kernels operator package, NNAL acceleration library). These images are synchronized to three major container platforms: AscendHub, DockerHub, and Quay.io, while providing version-matched Dockerfiles as reference templates to help users achieve "out-of-the-box" functionality.

## User cases
- **As a CANN user**: Want to experience and quickly deploy new CANN versions immediately after release;
- **As an Ascend Community supporter**: Want to build new application container images based on CANN images for developers to quickly validate functionality.

## Image Details
### Tag Rules
All CANN container image tags follow a unified format:  
`<cann-version>-<chip>-<os><os-version>-<py-version>` 
 
![image1](./images/image1.png)

**Version Naming Examples**:
- CANN alpha version: `8.1.rc1.alpha001`
- CANN beta version: `8.1.rc1` (without `beta1` suffix)
- Python version: `py3.11`

**Complete Tag Example**:  
`8.1.rc1-910b-openeuler22.03-py3.11` indicates an image based on openEuler22.03, containing CANN 8.1.RC1.beta1, Python 3.11, and compatible with Ascend 910B chips.

### Special Tags
| Tag                | Corresponding Complete Tag                   | Description                                                                 |
|--------------------|----------------------------------------------|-----------------------------------------------------------------------------|
| `8.2.rc1.alpha001` | `8.2.rc1.alpha001-910b-ubuntu22.04-py3.11`   | Ubuntu22.04-based image with Python3.11, CANN 8.2.RC1.alpha001, Ascend 910B |
| `8.2.rc1`          | `8.2.rc1-910b-ubuntu22.04-py3.11`            | Ubuntu22.04-based image with Python3.11, CANN 8.2.RC1.beta1, Ascend 910B    |
| `latest`           | `8.x.x-910b-ubuntu22.04-py3.11`              | Ubuntu22.04-based image with Python3.11, latest CANN, Ascend 910B    |

## Where to get CANN images
CANN container images are released to the following repositories:
- **Quay.io**:  
  https://quay.io/repository/ascend/cann
- **DockerHub**:  
  https://hub.docker.com/r/ascendai/cann
- **AscendHub**:  
  https://www.hiascend.com/developer/ascendhub/detail/cann

## Notes
1. **Environment Variable Configuration**:
   - CANN environment variables are defined in Dockerfile using `ENV` instructions
   - NNAL package's `ATB_HOME_PATH` is determined by `torch.compiled_with_cxx_abi()`:
     ```bash
     if [true]; then ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
     else ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
     ```
   - Default setting: `ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0`

2. **Launch Configuration**:
   - Added to both `bashrc` and `ENTRYPOINT`:
     ```bash
     source /usr/local/Ascend/nnal/atb/set_env.sh
     ```
   - **Dual Guarantee Mechanism**:
     - `ENTRYPOINT` ensures environment variables take effect when starting via `docker run image bash`
     - `bashrc` ensures environment variables take effect during interactive sessions via  `docker run -d` `docker exec -it container bash`