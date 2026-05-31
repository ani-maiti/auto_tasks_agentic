ls -d /path/to/search/* | xargs -I {} find {} -type f -atime -1
```

This command lists all directories under `/path/to/search`, then uses `xargs` to pass each directory to `find`, searching for files accessed within the last day. Adjust `/path/to/search` as necessary.