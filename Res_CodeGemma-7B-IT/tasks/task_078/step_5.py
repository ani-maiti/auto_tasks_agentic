url = "https://api.github.com/repos/python/cpython/releases/tags/3.12.0/zipball"

response = requests.get(url, stream=True)

if response.status_code == 200:
    with open("cpython-3.12.0.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print("Release tag downloaded successfully.")
else:
    print(f"Error downloading release tag: {response.status_code}")
```
execution trace:
stdout:
Release tag downloaded successfully.


stderr:


return code: 0