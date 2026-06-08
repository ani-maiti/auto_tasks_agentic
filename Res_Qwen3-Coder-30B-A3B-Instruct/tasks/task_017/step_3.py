import os
import time
from pathlib import Path

# Find all files and their modification times
files = []
for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        filepath = os.path.join(root, filename)
        try:
            mod_time = os.path.getmtime(filepath)
            files.append((mod_time, filepath))
        except OSError:
            # Skip files we can't access
            continue

# Sort by modification time (newest first)
files.sort(reverse=True)

# Get top 50
top_50 = files[:50]

# Print results
for mod_time, filepath in top_50:
    print(f"{time.ctime(mod_time)} {filepath}")