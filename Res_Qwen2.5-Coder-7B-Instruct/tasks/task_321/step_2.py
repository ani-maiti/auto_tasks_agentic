import os
import zipfile
from collections import defaultdict

# Step 2: Recursively search for archives in the current directory and subdirectories
def find_archives(directory):
    archives = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                archives.append(os.path.join(root, file))
    return archives

archives = find_archives('.')

print(f"Found {len(archives)} archives.")