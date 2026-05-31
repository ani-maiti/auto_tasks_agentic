import os

def find_zero_byte_files(directory):
    zero_byte_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:
                zero_byte_files.append(file_path)
    return zero_byte_files

directory_to_search = "/path/to/search"
zero_byte_files = find_zero_byte_files(directory_to_search)

if zero_byte_files:
    print("Zero-byte files found:")
    for file in zero_byte_files:
        print(file)
else:
    print("No zero-byte files found.")
```

Replace `/path/to/search` with the actual directory you want to search for zero-byte files. This script will walk through the specified directory and its subdirectories, identifying and listing all files that are zero bytes in size.