url = "https://api.github.com/repos/python/cpython/releases"

response = requests.get(url)

if response.status_code == 200:
    releases = response.json()
    latest_release = releases[0]
    release_tag = latest_release["tag_name"]
    print(f"Latest release tag: {release_tag}")
else:
    print(f"Error fetching releases: {response.status_code}")
```
execution trace:
stdout:
Latest release tag: 3.12.0


stderr:


return code: 0