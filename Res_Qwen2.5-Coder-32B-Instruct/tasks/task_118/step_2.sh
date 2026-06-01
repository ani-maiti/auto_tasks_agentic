echo "Curl is already installed. Fetching the latest release version from GitHub..."
curl -s https://api.github.com/repos/curl/curl/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'