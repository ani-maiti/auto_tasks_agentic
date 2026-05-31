import requests

response = requests.get("https://registry.hub.docker.com/v2/repositories/docker/docker/tags")

latest_tag = None
max_version = float('-inf')

for tag in response.json():
    tag_version = float(tag['name'].replace('.', ''))
    if tag_version > max_version:
        max_version = tag_version
        latest_tag = tag['name']

print(latest_tag)