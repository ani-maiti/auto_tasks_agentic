find . -type f | grep '\.\.' > files_with_multiple_dots.txt
```

This command finds all files (`-type f`) in the current directory and its subdirectories, filters out those with more than one dot in their names using `grep`, and saves the results to `files_with_multiple_dots.txt`.