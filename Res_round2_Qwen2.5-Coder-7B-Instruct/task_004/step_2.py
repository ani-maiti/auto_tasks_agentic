import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
duplicate_files = {f: files.count(f) for f in files if files.count(f) > 1}
for file, count in duplicate_files.items():
    print(f"Duplicate file: {file} ({count} occurrences)")