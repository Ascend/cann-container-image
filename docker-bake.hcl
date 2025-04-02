variable "registry" {
  default = []
}
variable "cann" {
  default = []
}

function "generate_tags" {
  params = [repo, tags]
  result = flatten([
    for reg in registry : [
      contains(keys(tags), reg.name) ? [
        for tag in tags[reg.name] : [
          "${reg.url}/${reg.owner}/${repo}:${tag}"
        ]
      ]
      : [
        for tag in tags["common"] : [
          "${reg.url}/${reg.owner}/${repo}:${tag}"
        ]
      ]
    ]
  ])
}

group "default" {
  targets = ["cann"]
}

target "docker-metadata-action" {
}

target "cann" {
  inherits = ["docker-metadata-action"]
  platforms = ["linux/amd64", "linux/arm64"]
  name = replace("cann-${item.tags.common[0]}", ".", "_")
  context = "cann/${item.tags.common[0]}/"
  dockerfile = "dockerfile"
  matrix = {
    item = cann
  }
  tags = generate_tags("cann", "${item.tags}")
}

