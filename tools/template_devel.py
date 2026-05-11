import os
import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('tools/template'))
          
def render_and_save_cann_dockerfile(args, ubuntu_template, openeuler_template):
    if "cann" not in args or not args["cann"]:
        return
    
    for item in args["cann"]:
        if item["os_name"] == "ubuntu":
            template_name = ubuntu_template
        else:
            template_name = openeuler_template
            
        template = env.get_template(template_name)

        rendered_content = template.render(item=item)

        output_path = os.path.join(
            "cann",
            f"{item['tag']}-devel",
            "Dockerfile"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(rendered_content)
        print(f"Generated: {output_path}")
        
def main():  
    with open('build_cann_devel_arg.json', 'r') as f:
        args = json.load(f)
    render_and_save_cann_dockerfile(args, "ubuntu.devel.Dockerfile.j2", "openeuler.devel.Dockerfile.j2")

if __name__ == "__main__":
    main()

