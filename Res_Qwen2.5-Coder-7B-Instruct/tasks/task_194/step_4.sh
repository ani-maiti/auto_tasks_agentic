echo "/path/to/search" | tr ' ' '\n' | xargs -I {} sh -c 'test -d "{}" && find "{}" -type f -atime -1'
```

This command checks if each item under `/path/to/search` is a directory and, if so, runs `find` to locate files accessed within the last day. Adjust `/path/to/search` as needed.