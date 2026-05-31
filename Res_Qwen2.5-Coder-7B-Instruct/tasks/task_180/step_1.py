import os
import hashlib

def calculate_sha256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = calculate_sha256(file_path)
            if hash_value in file_hashes:
                file_hashes[hash_value].append(file_path)
            else:
                file_hashes[hash_value] = [file_path]
    duplicates = {hash_value: paths for hash_value, paths in file_hashes.items() if len(paths) > 1}
    return duplicates

directory_to_search = '/path/to/search'
duplicates = find_duplicate_files(directory_to_search)

for hash_value, paths in duplicates.items():
    print(f"Duplicate files with SHA256 hash {hash_value}:")
    for path in paths:
        print(path)
```

This script calculates the SHA256 hash for all files in a specified directory and identifies any files that have the same hash, indicating they are likely duplicates. Replace `/path/to/search` with the actual directory you want to scan. The script will then print out the paths of any duplicate files found.