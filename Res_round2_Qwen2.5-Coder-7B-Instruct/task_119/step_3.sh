echo "Fetching latest release version of Git from GitHub..."
curl --silent "https://api.github.com/repos/git/git/releases/latest" | grep '"tag_name":' | sed 's/.*"\(.*\)"..*/\1/' > latest_release.txt
cat latest_release.txt