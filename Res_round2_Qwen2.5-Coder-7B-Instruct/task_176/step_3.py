import subprocess

# Run the previous command to get the file extensions
result = subprocess.run(['find', '.', '-type', 'f'], capture_output=True, text=True)
stdout = result.stdout

# Extract file extensions from the output
extensions = [line.split()[-1] for line in stdout.strip().split('\n') if '.' in line]

# Count the frequency of each extension
extension_counts = Counter(extensions)

# Sort extensions by frequency
sorted_extensions = extension_counts.most_common()

# Print the sorted list of extensions
for ext, count in sorted_extensions:
    print(f"{ext}: {count}")