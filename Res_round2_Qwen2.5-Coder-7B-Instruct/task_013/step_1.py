import os
import glob

# Find all Python files in the current directory and its subdirectories
python_files = glob.glob('**/*.py', recursive=True)

# Initialize a counter for the occurrences of 'import'
import_count = 0

# Iterate over each file and count occurrences of 'import'
for file_path in python_files:
    with open(file_path, 'r') as file:
        content = file.read()
        import_count += content.count('import')

print(f'Total occurrences of "import": {import_count}')