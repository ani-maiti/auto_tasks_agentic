import requests

url = "https://api.github.com/repos/rust-lang/rust/releases/latest"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    release_version = data["tag_name"]
    print(f"Latest Rust release version: {release_version}")
else:
    print("Failed to retrieve release version.")