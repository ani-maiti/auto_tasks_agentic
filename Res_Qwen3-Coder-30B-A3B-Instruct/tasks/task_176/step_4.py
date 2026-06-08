import os
from collections import Counter

# Get all files with extensions
extensions = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if '.' in file:
            ext = file.split('.')[-1]
            extensions.append(ext)

# Count frequencies
ext_counts = Counter(extensions)

# Sort by frequency
sorted_exts = sorted(ext_counts.items(), key=lambda x: x[1], reverse=True)

# Print report
print("File Extension Report (sorted by frequency):")
print("-" * 40)
for ext, count in sorted_exts:
    print(f"{ext}: {count}")