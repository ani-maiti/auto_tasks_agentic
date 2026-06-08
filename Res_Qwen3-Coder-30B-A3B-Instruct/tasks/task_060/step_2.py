import json
import urllib.request

url = "https://api.github.com/repos/rust-lang/rust/releases/latest"
with urllib.request.urlopen(url) as response:
    data = response.read()
    release_info = json.loads(data)
    print(release_info['tag_name'])