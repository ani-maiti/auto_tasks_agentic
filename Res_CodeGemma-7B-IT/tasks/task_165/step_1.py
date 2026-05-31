import os

# Get the list of files in the current directory
files = os.listdir('.')

# Create a list of file sizes
file_sizes = []
for file in files:
    file_path = os.path.join('.', file)
    file_sizes.append(os.path.getsize(file_path))

# Sort the file sizes in ascending order
file_sizes.sort()

# Find the middle index
mid = len(file_sizes) // 2

# If the number of files is even, the median is the average of the two middle files
if len(file_sizes) % 2 == 0:
    median = (file_sizes[mid] + file_sizes[mid - 1]) / 2
# Otherwise, the median is the value at the middle index
else:
    median = file_sizes[mid]

# Print the median file size
print(median)