import requests

url = "https://api.github.com/repos/git/git/releases/latest"
response = requests.get(url)

if response.status_code == 200:
    release_data = response.json()
    release_version = release_data["tag_name"]
    print(f"Latest release version: {release_version}")
else:
    print("Failed to fetch release data")
```
execution trace:
stdout:
Latest release version: v2.40.2


stderr:


return code: 0