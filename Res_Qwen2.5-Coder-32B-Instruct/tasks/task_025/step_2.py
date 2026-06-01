import json
from pathlib import Path

file_sizes = {}
with open('file_sizes.txt', 'r') as f:
    for line in f:
        size, path = line.strip().split(maxsplit=1)
        file_sizes[str(Path(path).resolve())] = size

json_output = json.dumps(file_sizes, indent=4)
print(json_output)