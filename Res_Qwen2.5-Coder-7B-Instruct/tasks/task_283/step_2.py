import os
import json

# Find all Python files in the current directory tree
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))
print(f"Found {len(python_files)} Python files.")