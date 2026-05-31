import os

def get_directory_size(directory):
  total_size = 0
  for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
      file_path = os.path.join(dirpath, filename)
      total_size += os.path.getsize(file_path)
  return total_size

# Get the list of directories
directories = os.listdir()

# Calculate the size of each directory
directory_sizes = []
for directory in directories:
  directory_size = get_directory_size(directory)
  directory_sizes.append((directory, directory_size))

# Sort the directories by size in descending order
directory_sizes.sort(key=lambda x: x[1], reverse=True)

# Get the directory with the largest size
largest_directory = directory_sizes[0][0]

# Print the largest directory
print(largest_directory)