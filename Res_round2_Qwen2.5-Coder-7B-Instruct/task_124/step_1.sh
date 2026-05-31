curl -s https://api.github.com/repos/numpy/numpy | jq '.stargazers_count'
```

This command uses `curl` to fetch the JSON data for the numpy repository from GitHub's API and then pipes it to `jq`, a command-line JSON processor, to extract the number of stargazers.