curl -s https://api.github.com/search/repositories?q=language:rust&sort=stars&order=desc | jq '.items[0:5].{name: .name, stars: .stargazers_count}'
```

This command uses `curl` to fetch the JSON data from the GitHub API for repositories that are written in Rust, sorted by the number of stars in descending order. The `jq` tool is then used to parse the JSON and extract the name and star count of the top 5 repositories.