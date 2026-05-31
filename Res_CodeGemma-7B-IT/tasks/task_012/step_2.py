import os

# Get the current directory
cwd = os.getcwd()

# Search for files containing "TODO"
files = []
for filename in os.listdir(cwd):
    if filename.endswith(".py") or filename.endswith(".sh"):
        with open(filename, "r") as f:
            if "TODO" in f.read():
                files.append(filename)

# Print the list of files
print(files)
```
execution trace:
stdout:
['task.py']


stderr:


return code: 0