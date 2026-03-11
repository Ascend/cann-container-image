---
name: CANN Image Release Engineer
description: You are a software development engineer responsible for automating and executing the CANN Docker image release pipeline.
---

# CANN Image Release Process

## When to use this skill
Use this skill when a new CANN software version is released to generate all necessary code and configuration for building and publishing the corresponding Docker images.

## Release Workflow

### Step 1: Update Alpha/Beta Version Template (Conditional)
Action: Check if the specified CANN version string contains "alpha" or "beta".

If YES: Update the ALPHA_DICT mapping within `/tools/template.py`. Add a new entry using the CANN version as the key and its corresponding download link identifier as the value.

If NO: Proceed to Step 2. No changes to template.py are required.

### Step 2: Generate Build Configuration for Standard Environments
Action: Modify the `build_cann_arg.json` file.

Configuration Basis:

CANN Version: The newly specified version.

Target Chips (cann_chip): 910b, 310p, A3, 910

Operating Systems (os): openeuler (24.03), ubuntu (22.03)

Python Version (py-version): 3.11

Tag Naming Convention: <cann-version>-<chip>-<os><os-version>-<py-version>

Goal: Create a build matrix in the JSON file that covers all combinations of the above parameters for standard OS images.

### Step 3: Generate Build Configuration for ManyLinux Environments
Action: Modify the `build_manylinux_arg.json` file.
Configuration Basis:

CANN Version: The newly specified version.

Target Chips (cann_chip): 910b, 310p, A3

Operating System (os): manylinux (2_28)

Python Version (py-version): 3.11

Tag Naming Convention: <cann-version>-<chip>-<os><os-version>-<py-version>

Goal: Create a build matrix for the cross-platform manylinux compatibility images.

### Step 4: Execute Template Engine to Generate Dockerfiles
Action: Run the template engine script.

```
python3 tools/template.py
```

Outcome: This will generate the `cann/` and `manylinux/` directories containing the Dockerfiles and the finalized build_*_arg.json configuration files for the build process.

### Step 5: Register New Image Tags for Publication
Action: Update the version registry JSON files.

Update `cann_publish_version.json` with the new tags generated for standard environments.

Update `manylinux_publish_version.json` with the new tags generated for manylinux environments.

Purpose: This step registers the new version tags, making them available for the CI/CD pipeline to build and publish.

### Step 6:  Update CI/CD Workflow Definitions
Action: Edit the GitHub Actions workflow files.

Modify `.github/workflows/build_and_push_cann.yml`.

Modify `.github/workflows/build_and_push_manylinux.yml`.

Change Required: Add the newly generated image tags (from Step 2 & 3) to the list of valid inputs for the workflow_dispatch trigger. This allows the new images to be manually triggered for build.





