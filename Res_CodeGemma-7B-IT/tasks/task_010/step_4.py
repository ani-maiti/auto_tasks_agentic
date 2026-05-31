import os

json_files = [filename for filename in os.listdir(".") if filename.endswith(".json")]

print(len(json_files))
print(json_files)
```
execution trace:
stdout:


stderr:


return code: 0