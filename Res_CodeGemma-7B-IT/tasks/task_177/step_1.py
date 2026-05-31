import os

# Get the list of files in the current directory
files = os.listdir('.')

# Create a list of file sizes
file_sizes = [(file, os.path.getsize(file)) for file in files]

# Sort the file sizes in descending order
file_sizes.sort(key=lambda x: x[1], reverse=True)

# Print the top 100 largest files
for file, size in file_sizes[:100]:
    print(f"{file}: {size}")