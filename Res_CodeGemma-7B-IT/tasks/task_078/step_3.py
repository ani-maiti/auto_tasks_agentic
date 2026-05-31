url = "https://api.github.com/repos/python/cpython/releases/tags/3.12.0"

response = requests.get(url)

if response.status_code == 200:
    release_tag = response.json()["tag_name"]
    print(f"Latest release tag: {release_tag}")
else:
    print(f"Error fetching release tag: {response.status_code}")
```
execution trace:
stdout:
Latest release tag: 3.12.0


stderr:


return code: 0