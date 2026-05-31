import os

# Get a list of all directories in the current directory
directories = [d for d in os.listdir(".") if os.path.isdir(d)]

# Calculate the total size of each directory
directory_sizes = {}
for directory in directories:
    total_size = 0
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        total_size += os.path.getsize(file_path)
    directory_sizes[directory] = total_size

# Sort the directories by total size in descending order
sorted_directories = sorted(directory_sizes.items(), key=lambda x: x[1], reverse=True)

# Print a report of the sorted directories
print("Directory Report:")
for directory, size in sorted_directories:
    print(f"{directory:<20s} {size:>10d}")