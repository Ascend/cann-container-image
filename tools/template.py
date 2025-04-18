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
    "8.1.RC1.alpha001": "V100R001C21B800TP034"
}

env = Environment(loader=FileSystemLoader("tools/template"))

def generate_file_prefix(prefix, version, suffix="linux"):
    return f"{prefix}_{version}_{suffix}"

def generate_url(base_url, path, file_prefix):
    return f"{base_url}/{path}/{file_prefix}"

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
    
    toolkit_file_prefix = generate_file_prefix("Ascend-cann-toolkit", version)
    kernels_file_prefix = generate_file_prefix(f"Ascend-cann-kernels-{cann_chip}", version)
    nnal_file_prefix = generate_file_prefix("Ascend-cann-nnal", nnal_version)
    
    cann_toolkit_url_prefix = generate_url(url_prefix, "", toolkit_file_prefix)
    cann_kernels_url_prefix = generate_url(url_prefix, "", kernels_file_prefix)
    cann_nnal_url_prefix = generate_url(nnal_url_prefix, "", nnal_file_prefix)
    
    return cann_toolkit_url_prefix, cann_kernels_url_prefix, cann_nnal_url_prefix
    
def render_and_save_dockerfile(template_name, item):
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
        item["cann_version"],
        f"{item['cann_chip']}-{item['os_name']}{item['os_version']}-py{item['py_version']}",
        "Dockerfile"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(rendered_content)
    print(f"Generated: {output_path}")

def process_dockerfile_args(args, ubuntu_template, openeuler_template):
    for arg in args["cann"]:
        if arg["os_name"] == "ubuntu":
            template = ubuntu_template
        else:
            template = openeuler_template
        render_and_save_dockerfile(template, arg)
        
def generate_tags(tags, registry):
    return [
        f"{reg['url']}/{reg['owner']}/cann:{tag}"
        for reg in registry
        for tag in tags.get(reg["name"], tags["common"])
    ]
    
def generate_targets(args):
    return [
        {
            "name": f"{arg['cann_version']}-{arg['cann_chip']}-{arg['os_name']}{arg['os_version']}-py{arg['py_version']}",
            "context": os.path.join(
                "cann", 
                arg["cann_version"],
                f"{arg['cann_chip']}-{arg['os_name']}{arg['os_version']}-py{arg['py_version']}"
            ),
            "dockerfile": "Dockerfile",
            "tags": ",".join(generate_tags(arg["tags"], args["registry"])),
        }
        for arg in args["cann"]
    ]

def render_and_save_workflow(args, workflow_template):
    targets = generate_targets(args)
    template = env.get_template(workflow_template)
    rendered_content = template.render(targets=targets, cann_version=args["cann"][0]["cann_version"])
    
    output_path = os.path.join(".github", "workflows", f"build_{args['cann'][0]['cann_version']}.yml")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(rendered_content)
    print(f"Generated: {output_path}")

def main():  
    with open("arg.json", "r") as f:
        args = json.load(f)
    process_dockerfile_args(args, "ubuntu.Dockerfile.j2", "openeuler.Dockerfile.j2")
    render_and_save_workflow(args, "docker_template.yml.j2")


if __name__ == "__main__":
    main()