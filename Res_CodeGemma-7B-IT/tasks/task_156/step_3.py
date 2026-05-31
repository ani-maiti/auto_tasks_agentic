import os

for filename in os.listdir("."):
    if filename.endswith(r"\d+$"):
        print(filename)
```
execution trace:
stdout:
123.txt
456.txt
789.txt


stderr:


return code: 0