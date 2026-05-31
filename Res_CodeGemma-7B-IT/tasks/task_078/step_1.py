import requests

url = "https://api.github.com/repos/python/cpython/releases/latest"

response = requests.get(url)

if response.status_code == 200:
    release_tag = response.json()["tag_name"]
    print(f"Latest release tag: {release_tag}")
else:
    print(f"Error fetching release tag: {response.status_code}")