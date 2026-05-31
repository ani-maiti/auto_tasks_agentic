find . -name "*.json" | wc -l
```

This command finds all files with the `.json` extension in the current directory and its subdirectories, then counts them. The `wc -l` part counts the number of lines, which corresponds to the number of JSON files found.