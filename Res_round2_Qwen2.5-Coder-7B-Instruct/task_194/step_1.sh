find /path/to/search -type f -amin -1440
```

This command searches for files (`-type f`) in the specified directory and its subdirectories that were accessed within the last 24 hours (1440 minutes). Adjust `/path/to/search` to the directory you want to search.