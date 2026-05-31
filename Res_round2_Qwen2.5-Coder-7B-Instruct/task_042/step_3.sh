find . -type f | grep -E '\b\d{4}-\d{2}-\d{2}\b' 2>&1 >/dev/null
```

This command redirects both standard error and standard output to `/dev/null` to suppress all output, including errors.