import os
from pathlib import Path

# Count unique file extensions in current directory and subdirectories
extension_count = {}
for file_path in Path('.').rglob('*'):
    if file_path.is_file():
        ext = file_path.suffix.lower()
        if ext:
            extension_count[ext] = extension_count.get(ext, 0) + 1

print(len(extension_count))