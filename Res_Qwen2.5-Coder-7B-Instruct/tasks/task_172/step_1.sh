find . -type f -name "*.txt" | xargs grep -oE 'https?://[^\s]+' > urls.txt
```

This command finds all `.txt` files in the current directory and its subdirectories, extracts URLs using `grep`, and saves them to a file named `urls.txt`.