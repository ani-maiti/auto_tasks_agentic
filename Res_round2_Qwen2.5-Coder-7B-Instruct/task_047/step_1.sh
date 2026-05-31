find . -type f | xargs grep -l '{.*}'
```

This command will search for all files (`find . -type f`) and then check if they contain a JSON object (`grep -l '{.*}'`). The `-l` option tells `grep` to only list the filenames where the pattern is found.