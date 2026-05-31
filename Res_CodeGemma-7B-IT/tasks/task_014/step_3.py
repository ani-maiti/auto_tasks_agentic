import os

for filename in os.listdir("."):
    if not filename.startswith("."):
        print(filename)
```
execution trace:
stdout:
nasa_seed
tasks

stderr:


return code: 0