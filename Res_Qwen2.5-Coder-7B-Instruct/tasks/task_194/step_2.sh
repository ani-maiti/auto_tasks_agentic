echo "/path/to/search" | tr ' ' '\n' | xargs -I {} find {} -type f -atime -1
```

This command first prints the path, then splits it into individual directories if there are spaces, and finally runs `find` on each directory to locate files accessed within the last day.