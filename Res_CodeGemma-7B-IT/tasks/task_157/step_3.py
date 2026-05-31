import os

for filename in os.listdir("."):
    if filename.isupper():
        print(filename)
    elif filename.islower():
        print(f"Ignoring file: {filename}")
    else:
        print(f"Unknown file type: {filename}")
```
execution trace:
stdout:
Ignoring file: file.txt
Ignoring file: test.py
Ignoring file: README.md
Unknown file type: task_157.py

stderr:


return code: 0