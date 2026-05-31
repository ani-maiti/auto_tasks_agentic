import requests

# Get the latest release from GitHub
response = requests.get("https://api.github.com/repos/neovim/neovim/releases/latest")

# Get the release version
release_version = response.json()["tag_name"]

# Print the release version
print(release_version)