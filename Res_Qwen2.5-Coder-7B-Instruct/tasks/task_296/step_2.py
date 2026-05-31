import os
import json

# Find all Python files in the current directory and its subdirectories
python_files = [os.path.join(root, file) for root, dirs, files in os.walk('.') for file in files if file.endswith('.py')]
print(python_files)