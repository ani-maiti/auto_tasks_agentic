import json
import subprocess

# Fetch the latest Kubernetes release tag using curl
result = subprocess.run(['curl', '-s', 'https://api.github.com/repos/kubernetes/kubernetes/releases/latest'], capture_output=True, text=True)
latest_tag = json.loads(result.stdout)['tag_name']

print(f"The latest Kubernetes release tag is: {latest_tag}")