import os

# List all files in the current directory and its subdirectories
all_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            all_files.append(os.path.join(root, file))

print(f"Found {len(all_files)} Python files.")