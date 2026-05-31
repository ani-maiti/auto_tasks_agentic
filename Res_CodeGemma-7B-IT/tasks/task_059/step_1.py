import requests

response = requests.get("https://api.github.com/repos/nodejs/node/releases/latest")

if response.status_code == 200:
    version = response.json()["tag_name"]
    print(f"Latest Node.js release version: {version}")
else:
    print(f"Error retrieving release version: {response.status_code}")