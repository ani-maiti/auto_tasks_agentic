find . -type f -exec ls -lh {} + | awk '{print $5 " " $9}' | sort | uniq -c | grep -v ' 1 '
```

This command finds all files in the current directory and its subdirectories, lists them with their sizes and paths, sorts them by size, counts occurrences of each size, and filters out those that appear only once.