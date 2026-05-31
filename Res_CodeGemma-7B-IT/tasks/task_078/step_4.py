url = "https://api.github.com/repos/python/cpython/releases/tags/3.12.0/zipball"

response = requests.get(url)

if response.status_code == 200:
    print("Release tag downloaded successfully.")
else:
    print(f"Error downloading release tag: {response.status_code}")
```
execution trace:
stdout:
Release tag downloaded successfully.


stderr:


return code: 0