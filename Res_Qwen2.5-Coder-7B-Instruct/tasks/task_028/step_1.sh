# List all files in the current directory and its subdirectories, sorted by size
find . -type f -exec ls -lh {} + | sort -k5 -hr | head -n 101 > largest_files.txt
```

This command finds all files (`-type f`), lists them with their sizes (`ls -lh`), sorts them by size in descending order (`sort -k5 -hr`), and takes the top 101 entries (including the header). The results are saved to `largest_files.txt`.