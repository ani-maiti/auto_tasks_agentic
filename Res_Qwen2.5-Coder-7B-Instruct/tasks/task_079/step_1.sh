curl -s https://api.github.com/repos/psf/requests | jq '.stargazers_count'
```

This command uses `curl` to fetch the JSON data for the requests repository from GitHub's API and then pipes it to `jq`, a lightweight and flexible command-line JSON processor, to extract the number of stargazers.