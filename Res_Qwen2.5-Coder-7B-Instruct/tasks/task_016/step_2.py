from collections import Counter

# Extract file extensions
extensions = [os.path.splitext(file)[1] for file in files]
extension_counts = Counter(extensions)

print(extension_counts)