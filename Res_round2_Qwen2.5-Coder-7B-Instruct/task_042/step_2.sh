find . -type f | grep -E '\b\d{4}-\d{2}-\d{2}\b' 2>/dev/null
```

This command redirects the error messages to `/dev/null` to suppress the warnings about backslashes in the regular expression.