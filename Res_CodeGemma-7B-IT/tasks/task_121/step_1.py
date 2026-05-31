import requests

url = "https://api.github.com/repos/tmux/tmux/releases/latest"
response = requests.get(url)

if response.status_code == 200:
    release_data = response.json()
    version = release_data["tag_name"]
    print(f"Latest tmux release: {version}")
else:
    print("Error fetching release data")