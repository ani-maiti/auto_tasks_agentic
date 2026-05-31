import os

# List all files in the current directory and subdirectories
files = []
for root, _, filenames in os.walk('.'):
    for filename in filenames:
        files.append(filename)

# Extract file extensions
extensions = [os.path.splitext(file)[1] for file in files if '.' in file]

# Count occurrences of each extension
extension_counts = {}
for ext in extensions:
    if ext in extension_counts:
        extension_counts[ext] += 1
    else:
        extension_counts[ext] = 1

# Find the least common extension
least_common_extension = min(extension_counts, key=extension_counts.get)
print(least_common_extension)