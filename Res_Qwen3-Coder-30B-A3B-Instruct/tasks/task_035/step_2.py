import os

# Read all file sizes and names
file_sizes = []
with open('/tmp/file_list.txt', 'w') as f:
    os.system('find . -type f -exec stat -c "%s %n" {} \\; > /tmp/file_list.txt')

with open('/tmp/file_list.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            size = int(parts[0])
            name = parts[1]
            file_sizes.append((size, name))

# Calculate average size
total_size = sum(size for size, _ in file_sizes)
count = len(file_sizes)
average_size = total_size / count if count > 0 else 0

print(f"Average file size: {average_size}")

# Find files larger than average
large_files = [(size, name) for size, name in file_sizes if size > average_size]

# Sort by size descending
large_files.sort(reverse=True)

# Print results
for size, name in large_files:
    print(f"{size} {name}")