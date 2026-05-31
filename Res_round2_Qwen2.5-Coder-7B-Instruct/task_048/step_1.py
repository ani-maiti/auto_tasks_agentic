import os

def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

# Example usage
directory_to_search = '/'
file_paths = get_all_file_paths(directory_to_search)
print(file_paths)
```

This script uses `os.walk` to traverse the directory tree starting from `/`, collecting all file paths into a list. The result is then printed. Adjust the `directory_to_search` variable as needed to target different directories.