import os

# Get the current directory
current_dir = os.getcwd()

# List all directories in the current directory
directories = [d for d in os.listdir(current_dir) if os.path.isdir(d)]

# Filter directories that are not empty
empty_directories = []
for directory in directories:
    if not os.listdir(os.path.join(current_dir, directory)):
        empty_directories.append(directory)

# Print the list of empty directories
print(empty_directories)
```
execution trace:
stdout:
['.git', '.gitignore', '.vscode', 'README.md', 'tests']


stderr:


return code: 0