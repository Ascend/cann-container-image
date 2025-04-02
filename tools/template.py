import os
import json
from jinja2 import Environment, FileSystemLoader

BASE_URL = "https://ascend-repo.obs.cn-east-2.myhuaweicloud.com"
ALPHA_DICT = {
    "8.0.RC2.alpha001": "V100R001C18B800TP015",
    "8.0.RC2.alpha002": "V100R001C18SPC805",
    "8.0.RC2.alpha003": "V100R001C18SPC703",
    "8.0.RC3.alpha002": "V100R001C19SPC702",
    "8.1.rc1.alpha001": "V100R001C21B800TP034"
}

env = Environment(loader=FileSystemLoader('tools/template'))

def get_download_url(cann_chip, version, nnal_version):
    if "alpha" in version:
        if version not in ALPHA_DICT:
            raise ValueError(f"Unsupported version: {version}. Supported versions are: {list(ALPHA_DICT.keys())}")
        url_prefix = BASE_URL + "/Milan-ASL/Milan-ASL%20" + ALPHA_DICT[version]
    else:
        url_prefix = BASE_URL + "/CANN/CANN%20" + version
        
    toolkit_file = "Ascend-cann-toolkit_" + version + "_linux-${ARCH}.run"
    kernels_file = "Ascend-cann-kernels-" + cann_chip + "_" + version + "_linux-${ARCH}.run"
    nnal_file = "Ascend-cann-nnal_" + nnal_version + "_linux-${ARCH}.run"
    
    cann_toolkit_url = f"{url_prefix}/{toolkit_file}"
    cann_kernels_url = f"{url_prefix}/{kernels_file}"   
    cann_nnal_url = f"{url_prefix}/{nnal_file}"
    return cann_toolkit_url, cann_kernels_url, cann_nnal_url
    
def render_and_save(template_name, item):
    template = env.get_template(template_name)
    cann_toolkit_url, cann_kernels_url, cann_nnal_url = get_download_url(item['cann_chip'], item['cann_version'], item['nnal_version'])
    item['cann_toolkit_url'] = cann_toolkit_url
    item['cann_kernels_url'] = cann_kernels_url
    item['cann_nnal_url'] = cann_nnal_url
    rendered_content = template.render(item=item)

    output_path = os.path.join("cann", item['tags']['common'][0], "dockerfile")
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