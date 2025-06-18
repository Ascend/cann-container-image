import os
import sys
import pytest
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.template import (
    get_python_download_url,
    get_cann_download_url,
    render_and_save_dockerfile,
    ALPHA_DICT
)

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('tools/template'))

@pytest.mark.parametrize("version", ["3.9"])
def test_get_python_download_url_success(version):
    package, url, latest_version = get_python_download_url(version)
    assert url.startswith(f"https://repo.huaweicloud.com/python/{version}.")
    assert url.endswith(".tgz")
    assert latest_version.startswith(version)

@pytest.mark.parametrize("version", ["99.0"])
def test_get_python_download_url_version_not_found(version):
    with pytest.raises(SystemExit) as pytest_exit:
        get_python_download_url(version)
    assert pytest_exit.type == SystemExit
    assert pytest_exit.value.code == 1

@pytest.mark.parametrize("version,chip", [
    ("8.1.RC1.alpha001", "310p"),
    ("8.1.RC1.alpha002", "310p"),
    ("8.1.RC1.alpha001", "910b"),
])
def test_get_cann_download_url_alpha_versions(version, chip):
    toolkit_url, kernels_url, nnal_url = get_cann_download_url(chip, version)
    
    assert f"Milan-ASL%20{ALPHA_DICT[version]}" in toolkit_url
    assert version in toolkit_url
    assert chip in kernels_url
    assert "Ascend-cann-nnal" in nnal_url
    
@pytest.mark.parametrize(
    "version, chip",
    [("8.0.0", "910b")] 
)
def test_get_cann_download_url_release(version, chip):
    toolkit_url, kernels_url, nnal_url = get_cann_download_url(chip, version)
    assert f"CANN%20{version}" in toolkit_url
    assert "Ascend-cann-toolkit" in toolkit_url
    assert f"ascend-cann-kernels-{chip.lower()}" in kernels_url.lower()
    assert "Ascend-cann-nnal" in nnal_url


TEST_CASES = [
    ("ubuntu", "22.04", "3.10", "910b", "8.0.0"),
    ("openeuler", "22.03", "3.9", "310p", "8.0.0"),
]
@pytest.mark.parametrize(
    "os_name, os_version, py_version, cann_chip, cann_version",
    TEST_CASES
)
def test_render_and_save_dockerfile_parametrized(
    os_name, os_version, py_version, cann_chip, cann_version
):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    original_cwd = os.getcwd()
    os.chdir(base_dir)

    test_args = {
        "cann": [
            {
                "os_name": os_name,
                "os_version": os_version,
                "py_version": py_version,
                "cann_chip": cann_chip,
                "cann_version": cann_version
            }
        ]
    }

    try:
        render_and_save_dockerfile(test_args, "ubuntu.Dockerfile.j2", "openeuler.Dockerfile.j2")

        output_path = os.path.join(
            "cann",
            f"{cann_version}-{cann_chip}-{os_name}{os_version}-py{py_version}",
            "Dockerfile"
        )

        assert os.path.exists(output_path), f"Dockerfile 未生成: {output_path}"
    finally:
        os.chdir(original_cwd)
        if os.path.exists("cann"):
            shutil.rmtree("cann")