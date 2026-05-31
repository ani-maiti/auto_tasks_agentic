find . -type f | grep -E '\b\d{4}-\d{2}-\d{2}\b'
```

This command searches for all files (`-type f`) in the current directory and its subdirectories (`find .`), then filters the results to show only those filenames that contain a date in the format `YYYY-MM-DD`. The `-E` option enables extended regular expressions, and `\b` ensures that the date is matched as a whole word.