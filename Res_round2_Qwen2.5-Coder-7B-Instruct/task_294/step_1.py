import os
import zipfile
from collections import defaultdict

# Step 1: Discover all archives in the current directory tree
archives = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.zip', '.rar', '.7z')):
            archives.append(os.path.join(root, file))

print(f"Found {len(archives)} archives.")