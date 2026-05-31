from pathlib import Path

count = 0

for entry in Path(".").glob("**/*"):
    if entry.is_dir():
        count += 1

print(count)
```
execution trace:
stdout:


stderr:


return code: 0