echo "/path/to/search" | xargs find . -type f -newermt $(date -d "1 day ago" +%Y-%m-%d)
```

This command finds files modified within the last day in the specified directory. Adjust `/path/to/search` to the directory you want to search.