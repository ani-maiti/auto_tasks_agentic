import requests

# Download the release asset
response = requests.get("https://github.com/neovim/neovim/releases/download/v0.12.2/nvim-linux64.tar.gz")

# Save the downloaded file
with open("nvim-linux64.tar.gz", "wb") as f:
    f.write(response.content)