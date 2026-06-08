import os
from collections import Counter

# Get all files in current directory and subdirectories
files = []
for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        files.append(os.path.join(root, filename))

# Extract extensions and count them
extensions = []
for file in files:
    _, ext = os.path.splitext(file)
    if ext:  # Only count files with extensions
        extensions.append(ext.lower())

# Count occurrences of each extension
extension_counts = Counter(extensions)

# Print results
print("File Extension Report:")
print("-" * 20)
for ext, count in extension_counts.most_common():
    print(f"{ext}: {count}")