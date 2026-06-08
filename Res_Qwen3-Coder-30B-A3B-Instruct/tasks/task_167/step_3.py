import os
import time
from pathlib import Path

# Get all files in current directory tree
files = []
for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        filepath = os.path.join(root, filename)
        # Get modification time
        mod_time = os.path.getmtime(filepath)
        files.append((mod_time, filepath))

# Sort by modification time (newest first)
files.sort(reverse=True)

# Print the 10 newest files
for i, (mod_time, filepath) in enumerate(files[:10]):
    print(f"{filepath} (modified: {time.ctime(mod_time)})")