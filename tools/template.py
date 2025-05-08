import os
import re
import requests
import json
from distutils.version import LooseVersion
from jinja2 import Environment, FileSystemLoader

BASE_URL = "https://ascend-repo.obs.cn-east-2.myhuaweicloud.com"
ALPHA_DICT = {
    "8.0.RC2.alpha001": "V100R001C18B800TP015",
    "8.0.RC2.alpha002": "V100R001C18SPC805",
    "8.0.RC2.alpha003": "V100R001C18SPC703",
    "8.0.RC3.alpha002": "V100R001C19SPC702",
    "8.1.RC1.alpha001": "V100R001C21B800TP034",
    "8.1.RC1.alpha002": "V100R001C21B800TP051",
}

env = Environment(loader=FileSystemLoader("tools/template"))

def get_python_download_url(version):  
    try:
        response = requests.get("https://www.python.org/ftp/python/")
        response.raise_for_status()
        versions = re.findall(rf"{version}\.[0-9]+", response.text)
        if not versions:
            print(f"[WARNING] Could not find the latest version for Python {version}")
            exit(1)
        py_latest_version = sorted(versions, key=LooseVersion)[-1]
        print(f"Latest Python version found: {py_latest_version}")
    
    except requests.RequestException as e:
        print(f"[WARNING] Error fetching Python versions: {e}")
        exit(1)
        
    py_installer_package = "Python-" + py_latest_version
    py_installer_url = os.path.join("https://repo.huaweicloud.com/python/", py_latest_version, py_installer_package + ".tgz")
    return py_installer_package, py_installer_url, py_latest_version
       
def get_cann_download_url(cann_chip, version, nnal_version):
    if "alpha" in version:
        if version not in ALPHA_DICT:
            raise ValueError(f"Unsupported version: {version}. Supported versions are: {list(ALPHA_DICT.keys())}")
        url_prefix = f"{BASE_URL}/Milan-ASL/Milan-ASL%20{ALPHA_DICT[version]}"
    else:
        url_prefix = f"{BASE_URL}/CANN/CANN%20{version}"
    
    nnal_url_prefix = f"{BASE_URL}/CANN/CANN%20{nnal_version}"
    
    toolkit_file_prefix = "Ascend-cann-toolkit_" + version + "_linux"
    kernels_file_prefix = "Ascend-cann-kernels-" + cann_chip + "_" + version + "_linux"
    nnal_file_prefix = "Ascend-cann-nnal_" + nnal_version + "_linux"
    
    cann_toolkit_url_prefix = f"{url_prefix}/{toolkit_file_prefix}"
    cann_kernels_url_prefix = f"{url_prefix}/{kernels_file_prefix}"   
    cann_nnal_url_prefix = f"{nnal_url_prefix}/{nnal_file_prefix}"
    
    return cann_toolkit_url_prefix, cann_kernels_url_prefix, cann_nnal_url_prefix

def render_and_save_dockerfile(args, ubuntu_template, openeuler_template):
    for item in args["cann"]:
        if item["os_name"] == "ubuntu":
            template_name = ubuntu_template
        else:
            template_name = openeuler_template
        template = env.get_template(template_name)
        py_installer_package, py_installer_url, py_latest_version = get_python_download_url(item["py_version"])
        item["py_installer_package"] = py_installer_package
        item["py_installer_url"] = py_installer_url
        item["py_latest_version"] = py_latest_version
        
        cann_toolkit_url_prefix, cann_kernels_url_prefix, cann_nnal_url_prefix = get_cann_download_url(
            item["cann_chip"], 
            item["cann_version"], 
            item["nnal_version"]
        )
        item["cann_toolkit_url_prefix"] = cann_toolkit_url_prefix
        item["cann_kernels_url_prefix"] = cann_kernels_url_prefix
        item["cann_nnal_url_prefix"] = cann_nnal_url_prefix
        
        rendered_content = template.render(item=item)
        
        output_path = os.path.join(
            "cann",
            f"{item['cann_version']}-{item['cann_chip']}-{item['os_name']}{item['os_version']}-py{item['py_version']}",
            "Dockerfile"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(rendered_content)
        print(f"Generated: {output_path}")
        
def generate_tags(tags, registry):
    ascendhub_tags = []
    common_tags = []
    for reg in registry:
        if reg["name"] == "ascendhub":
            for tag in tags["ascendhub"]:
                ascendhub_tags.append(f"{reg['url']}/{reg['owner']}/cann:{tag}")
        else:
            for tag in tags["common"]:
                common_tags.append(f"{reg['url']}/{reg['owner']}/cann:{tag}")
    return ascendhub_tags, common_tags

def generate_targets(args):
    return [
        {
            "name": f"{arg['cann_version']}-{arg['cann_chip']}-{arg['os_name']}{arg['os_version']}-py{arg['py_version']}",
            "context": os.path.join(
                "cann", 
                f"{arg['cann_version']}-{arg['cann_chip']}-{arg['os_name']}{arg['os_version']}-py{arg['py_version']}"
            ),
            "dockerfile": "Dockerfile",
            "ascendhub_tags": generate_tags(arg["tags"], args["registry"])[0],
            "common_tags": generate_tags(arg["tags"], args["registry"])[1]
        }
        for arg in args["cann"]
    ]
    
def generate_repos(args):
    repos = []
    ascend_repo = ""
    for registry in args["registry"]:
        if registry["name"] == "ascendhub":
            ascend_repo = registry["url"] + "/" + registry["owner"] + "/cann"
        else:
            repos.append(registry["url"] + "/" + registry["owner"] + "/cann")
    return repos, ascend_repo

def render_and_save_workflow(args, workflow_template):
    targets = generate_targets(args)
    repos, ascend_repo = generate_repos(args)
    for target in targets:
        template = env.get_template(workflow_template)
        rendered_content = template.render(target=target, repos=repos, ascend_repo= ascend_repo, cann_file=target['name'])
        output_path = os.path.join(".github", "workflows", f"build_{target['name'].replace('-', '_')}.yml")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(rendered_content)
        print(f"Generated: {output_path}")

def main():  
    with open("arg.json", "r") as f:
        args = json.load(f)
    render_and_save_dockerfile(args, "ubuntu.Dockerfile.j2", "openeuler.Dockerfile.j2")
    render_and_save_workflow(args, "docker_template.yml.j2")


if __name__ == "__main__":
    main()