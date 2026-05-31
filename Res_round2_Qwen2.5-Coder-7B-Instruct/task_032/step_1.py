import os
import hashlib

def md5(file_path):
    """Compute the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_python_files(directory):
    """Find all Python files in a directory recursively."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

# Example usage:
directory_to_search = '/path/to/your/project'
python_files = find_python_files(directory_to_search)

for file_path in python_files:
    print(f"MD5 hash of {file_path}: {md5(file_path)}")
```

This script defines two functions: `md5` to compute the MD5 hash of a file, and `find_python_files` to find all Python files in a given directory recursively. It then prints the MD5 hash of each Python file found in the specified directory. Replace `/path/to/your/project` with the actual path to your project directory.