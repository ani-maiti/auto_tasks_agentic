import os

def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.abspath(os.path.join(root, file)))
    return file_paths

# Example usage
directory_to_search = '/path/to/search'
file_paths = get_all_file_paths(directory_to_search)
print(file_paths)
```

This script uses `os.walk` to traverse the directory tree starting from `/path/to/search`. It collects all file paths and prints them. You need to replace `/path/to/search` with the actual directory you want to search.