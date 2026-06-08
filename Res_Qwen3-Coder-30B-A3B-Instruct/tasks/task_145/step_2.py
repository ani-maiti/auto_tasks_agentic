import os
import re

# Find all Python files that import pandas
pandas_import_pattern = re.compile(r'^\s*(import\s+pandas|from\s+pandas\s+import)', re.MULTILINE)

def check_file_for_pandas(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return bool(pandas_import_pattern.search(content))
    except Exception as e:
        # Handle files that can't be read
        return False

# Get all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

# Check each file for pandas import
pandas_files = []
for file in python_files:
    if check_file_for_pandas(file):
        pandas_files.append(file)

print('\n'.join(pandas_files))