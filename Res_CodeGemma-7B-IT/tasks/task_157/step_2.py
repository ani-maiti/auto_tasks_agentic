import os

for filename in os.listdir("."):
    if filename.isupper():
        print(filename)
    elif filename.islower():
        print(f"Ignoring file: {filename}")
```
execution trace:
stdout:
Ignoring file: file.txt
Ignoring file: test.py
Ignoring file: README.md

stderr:


return code: 0