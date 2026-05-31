import os

for filename in os.listdir("."):
    if not filename.startswith(".") and not filename.endswith(".py"):
        print(filename)
```
execution trace:
stdout:
tasks

stderr:


return code: 0