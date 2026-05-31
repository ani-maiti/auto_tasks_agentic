curl -s https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc | jq '.items[0:5]'
```

This command uses `curl` to fetch the JSON data from the GitHub API for searching repositories where the language is Python, sorted by stars in descending order. The `jq` tool is used to parse the JSON and extract the top 5 items. If `jq` is not installed, you can install it using your package manager (e.g., `sudo apt-get install jq` on Debian-based systems).