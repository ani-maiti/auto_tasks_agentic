curl -s https://hacker-news.firebaseio.com/v0/topstories.json | jq '.[:5]'
```

This command uses `curl` to fetch the top stories from Hacker News and then pipes it to `jq`, a lightweight and flexible command-line JSON processor, to extract the first five story IDs.