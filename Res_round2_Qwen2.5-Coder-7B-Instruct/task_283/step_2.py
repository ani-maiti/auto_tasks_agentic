import os
import glob

# Find all Python files in the current directory tree
python_files = glob.glob('**/*.py', recursive=True)
print(f"Found {len(python_files)} Python files.")