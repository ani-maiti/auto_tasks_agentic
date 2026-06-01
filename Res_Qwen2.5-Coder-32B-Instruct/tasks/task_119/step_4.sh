echo "Fetching the latest release version of git from GitHub..."
curl -s https://api.github.com/repos/git/git/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'