import json
from pathlib import Path

file_sizes = {}
with open('file_sizes.txt', 'r') as f:
    for line in f:
        size, path = line.strip().split(maxsplit=1)
        file_sizes[str(Path(path).resolve())] = size

with open('file_summary.json', 'w') as json_file:
    json.dump(file_sizes, json_file, indent=4)

print("JSON summary generated.")