import os
from collections import Counter

# Get all files with extensions
extensions = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if '.' in file:
            ext = file.split('.')[-1]
            extensions.append(ext)

# Count occurrences
ext_counts = Counter(extensions)

# Find minimum count
min_count = min(ext_counts.values())

# Find all extensions with minimum count
least_common = [ext for ext, count in ext_counts.items() if count == min_count]

print(f"Least common extensions: {least_common}")
print(f"Count: {min_count}")