echo "Fetching latest release tag from GitHub CLI repository using curl"
curl -s https://api.github.com/repos/cli/cli/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'