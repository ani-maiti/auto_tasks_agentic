import os

def find_python_files_with_requests(directory):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if 'requests' in content:
                            matching_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return matching_files

# Specify the directory to search
directory_to_search = '/path/to/search'

matching_files = find_python_files_with_requests(directory_to_search)

if matching_files:
    print("Python files containing 'requests':")
    for file in matching_files:
        print(file)
else:
    print("No Python files containing 'requests' found.")
```

Replace `/path/to/search` with the actual directory you want to search. This script will walk through the specified directory and its subdirectories, checking each `.py` file to see if it contains the word "requests". If it does, the file path will be added to the list `matching_files`. Finally, it will print out all the matching file paths.