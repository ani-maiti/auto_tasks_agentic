import os

# List all files in the current directory and its subdirectories
files = []
for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.py'):
            files.append(os.path.join(root, filename))

print(f"Found {len(files)} Python files.")