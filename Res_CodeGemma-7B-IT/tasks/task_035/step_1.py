import os

# Calculate the average file size
total_size = 0
num_files = 0
for filename in os.listdir():
    if os.path.isfile(filename):
        total_size += os.path.getsize(filename)
        num_files += 1
average_size = total_size / num_files

# Find all files larger than the average size
large_files = []
for filename in os.listdir():
    if os.path.isfile(filename) and os.path.getsize(filename) > average_size:
        large_files.append(filename)

# Print the list of large files
print(large_files)