import os
import glob

# Find all Python files in the current directory tree
python_files = glob.glob('**/*.py', recursive=True)
print(f"Found {len(python_files)} Python files.")

project_inventory = {}
for file in python_files:
    project_inventory[file] = extract_info(file)

print("Project inventory extracted.")