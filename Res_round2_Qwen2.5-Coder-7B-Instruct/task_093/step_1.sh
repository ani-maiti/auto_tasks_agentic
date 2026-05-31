curl -s https://api.github.com/search/repositories?q=language:rust&sort=stars&order=desc | jq '.items[0:5]'
```

This command uses `curl` to fetch the JSON data for the top 5 most starred Rust repositories from the GitHub API and then pipes it to `jq` to extract and display just the first five items. If `jq` is not installed, you can install it using your package manager.