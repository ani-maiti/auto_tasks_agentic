from collections import Counter
import os

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Extract file extensions
extensions = [os.path.splitext(file)[1] for file in files]
extension_counts = Counter(extensions)

print(extension_counts)