import os
from collections import Counter

# List all files in the current directory and its subdirectories
files = []
for root, _, filenames in os.walk('.'):
    for filename in filenames:
        files.append(filename)

# Extract file extensions
extensions = [os.path.splitext(file)[1] for file in files if '.' in file]

# Count occurrences of each extension
extension_counts = Counter(extensions)

# Find the least common extension
least_common_extension = extension_counts.most_common()[-1][0]

print(f"The least common filename extension is: {least_common_extension}")