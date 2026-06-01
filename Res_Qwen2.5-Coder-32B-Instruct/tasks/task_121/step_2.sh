echo "Fetching the latest release version of tmux from GitHub..."
curl -s https://api.github.com/repos/tmux/tmux/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'