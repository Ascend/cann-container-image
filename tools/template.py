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

env = Environment(loader=FileSystemLoader('tools/template'))

def get_python_download_url(version):  
    try:
        response = requests.get("https://www.python.org/ftp/python/")
        response.raise_for_status()
        versions = re.findall(rf"{version}\.[0-9]+", response.text)
        if not versions:
            print(f"[WARNING] Could not find the latest version for Python {version}")
            exit(1)
        latest_version = sorted(versions, key=LooseVersion)[-1]
        print(f"Latest Python version found: {latest_version}")
    
    except requests.RequestException as e:
        print(f"[WARNING] Error fetching Python versions: {e}")
        exit(1)
        
    py_installer_tgz = "Python-" + latest_version
    py_installer_url =  os.path.join("https://repo.huaweicloud.com/python/", latest_version, py_installer_tgz + ".tgz")
    return py_installer_tgz, py_installer_url
       
def get_cann_download_url(cann_chip, version, nnal_version):
    if "alpha" in version:
        if version not in ALPHA_DICT:
            raise ValueError(f"Unsupported version: {version}. Supported versions are: {list(ALPHA_DICT.keys())}")
        url_prefix = BASE_URL + "/Milan-ASL/Milan-ASL%20" + ALPHA_DICT[version]
    else:
        url_prefix = BASE_URL + "/CANN/CANN%20" + version
        
    nnal_url_prefix = BASE_URL + "/CANN/CANN%20" + nnal_version
        
    toolkit_file_prefix = "Ascend-cann-toolkit_" + version + "_linux"
    kernels_file_prefix = "Ascend-cann-kernels-" + cann_chip + "_" + version + "_linux"
    nnal_file_prefix = "Ascend-cann-nnal_" + nnal_version + "_linux"
    
    cann_toolkit_url_prefix = f"{url_prefix}/{toolkit_file_prefix}"
    cann_kernels_url_prefix = f"{url_prefix}/{kernels_file_prefix}"   
    cann_nnal_url_prefix = f"{nnal_url_prefix}/{nnal_file_prefix}"
    return cann_toolkit_url_prefix, cann_kernels_url_prefix, cann_nnal_url_prefix
    
def render_and_save(template_name, item):
    template = env.get_template(template_name)
    
    py_installer_tgz, py_installer_url = get_python_download_url(item['py_version'])
    item['py_installer_tgz'] = py_installer_tgz
    item['py_installer_url'] = py_installer_url
    
    cann_toolkit_url_prefix, cann_kernels_url_prefix, cann_nnal_url_prefix = get_cann_download_url(
        item['cann_chip'], 
        item['cann_version'], 
        item['nnal_version']
        )
    item['cann_toolkit_url_prefix'] = cann_toolkit_url_prefix
    item['cann_kernels_url_prefix'] = cann_kernels_url_prefix
    item['cann_nnal_url_prefix'] = cann_nnal_url_prefix
    
    rendered_content = template.render(item=item)

    output_path = os.path.join("cann", item['tags']['common'][0], "Dockerfile")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(rendered_content)
    print(f"Generated: {output_path}")

def process_args(args, ubuntu_template, openeuler_template):
    for arg in args["cann"]:
        if arg["os_name"] == "ubuntu":
            template = ubuntu_template
        else:
            template = openeuler_template
        render_and_save(template, arg)

def main():  
    with open('arg.json', 'r') as f:
        args = json.load(f)
    process_args(args, 'ubuntu.Dockerfile.j2', 'openeuler.Dockerfile.j2')


if __name__ == "__main__":
    main()