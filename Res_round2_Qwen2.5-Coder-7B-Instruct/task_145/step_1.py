import os

# Define the directory to search for Python files
search_directory = '/path/to/search'

# List all files in the directory
files = [f for f in os.listdir(search_directory) if os.path.isfile(os.path.join(search_directory, f))]

# Filter out Python files
py_files = [f for f in files if f.endswith('.py')]

# Initialize a list to store files that import pandas
pandas_imports = []

# Check each Python file for imports
for py_file in py_files:
    file_path = os.path.join(search_directory, py_file)
    with open(file_path, 'r') as file:
        content = file.read()
        if 'import pandas' in content or 'from pandas' in content:
            pandas_imports.append(py_file)

# Print the list of files that import pandas
print(pandas_imports)
```

This script will search for all Python files in the specified directory and check if they import pandas. It will then print a list of files that import pandas. Make sure to replace `/path/to/search` with the actual path where you want to search for Python files.