import os
import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('tools/template'))

def generate_registry_tags(tags, registry):
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
            "os_name": arg["os_name"],
            "ascendhub_registry_tags": generate_registry_tags(arg["tags"], args["registry"])[0],
            "common_registry_tags": generate_registry_tags(arg["tags"], args["registry"])[1]
        }
        for arg in args["cann"]
    ]
    
def generate_repos(args):
    repos = []
    ascendhub_repo = ""
    for registry in args["registry"]:
        if registry["name"] == "ascendhub":
            ascendhub_repo = registry["url"] + "/" + registry["owner"] + "/cann"
        else:
            repos.append(registry["url"] + "/" + registry["owner"] + "/cann")
    return repos, ascendhub_repo

def render_and_save_workflow(args, workflow_template):
    targets = generate_targets(args)
    repos, ascendhub_repo = generate_repos(args)
    for target in targets:
        template = env.get_template(workflow_template)
        rendered_content = template.render(target=target, repos=repos, ascendhub_repo=ascendhub_repo, cann_file=target['name'])
        output_path = os.path.join(".github", "workflows", f"build_{target['name'].replace('-', '_')}.yml")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(rendered_content)
        print(f"Generated: {output_path}")

def main():  
    with open('arg.json', 'r') as f:
        args = json.load(f)
    render_and_save_workflow(args, "docker_template.yml.j2")


if __name__ == "__main__":
    main()