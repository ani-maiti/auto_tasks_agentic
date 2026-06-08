import json
import urllib.request

# Fetch the latest release information from GitHub API
url = "https://api.github.com/repos/tmux/tmux/releases/latest"
with urllib.request.urlopen(url) as response:
    data = response.read()
    release_info = json.loads(data)

# Extract and print the version tag
version = release_info.get('tag_name', 'Unknown')
print(version)