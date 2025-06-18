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
    assert url.startswith("https://repo.huaweicloud.com/python/3.9.")
    assert url.endswith(".tgz")
    assert latest_version.startswith("3.9.")

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

def test_render_and_save_dockerfile():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 切换当前工作目录到项目根目录，以便 Jinja2 能找到 tools/template
    original_cwd = os.getcwd()
    os.chdir(base_dir)
    try:
        test_args = {
            "cann": [
                {
                    "os_name": "ubuntu",
                    "os_version": "22.04",
                    "py_version": "3.8",
                    "cann_chip": "910b",
                    "cann_version": "8.0.0"
                }
            ]
        }
        render_and_save_dockerfile(test_args, "ubuntu.Dockerfile.j2", "openeuler.Dockerfile.j2")

        output_path = os.path.join(
            "cann",
            "8.0.0-910b-ubuntu22.04-py3.8",
            "Dockerfile"
        )
        assert os.path.exists(output_path), "Dockerfile 未生成"
    finally:
        # 恢复原工作目录
        os.chdir(original_cwd)  
        if os.path.exists("cann"):
            shutil.rmtree("cann")