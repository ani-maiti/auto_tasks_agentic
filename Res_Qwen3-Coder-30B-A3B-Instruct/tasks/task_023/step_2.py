import os
from collections import Counter

# Count file extensions in current directory recursively
extensions = []
for root, dirs, files in os.walk('.'):
    for file in files:
        _, ext = os.path.splitext(file)
        if ext:
            extensions.append(ext.lower())

# Get unique extensions and count them
unique_extensions = set(extensions)
print(len(unique_extensions))