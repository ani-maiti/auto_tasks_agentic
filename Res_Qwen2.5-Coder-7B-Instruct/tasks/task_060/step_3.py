import json
import subprocess

response = subprocess.run(['curl', '--silent', 'https://api.github.com/repos/rust-lang/rust/releases/latest'], capture_output=True, text=True)
data = json.loads(response.stdout)
latest_version = data['tag_name']
print("The latest Rust release version is:", latest_version)