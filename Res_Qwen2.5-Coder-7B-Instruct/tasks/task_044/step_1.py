import os

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filter out empty files
non_empty_files = [f for f in files if os.path.getsize(f) > 0]

# Sort files by size
sorted_files = sorted(non_empty_files, key=os.path.getsize)

# Print the smallest non-empty file
if sorted_files:
    print(sorted_files[0])
else:
    print("No non-empty files found.")