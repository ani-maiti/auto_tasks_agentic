python3 -c "
import json
with open('file_list.txt', 'r') as f:
    lines = f.readlines()

files = {}
for line in lines:
    parts = line.strip().split(' ', 1)
    if len(parts) == 2:
        size, path = parts
        if size not in files:
            files[size] = []
        files[size].append(path)

duplicates = {size: paths for size, paths in files.items() if len(paths) > 1}

for size, paths in duplicates.items():
    print(f'Size: {size}')
    for path in paths:
        print(f'  {path}')
    print()
"