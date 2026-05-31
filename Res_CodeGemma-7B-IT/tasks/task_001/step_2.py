import heapq

# Get the list of files in the current directory
files = [f for f in os.listdir(".") if os.path.isfile(f)]

# Create a list of tuples containing the file name and size
file_sizes = [(f, os.path.getsize(f)) for f in files]

# Sort the files in descending order of size
file_sizes.sort(key=lambda f: f[1], reverse=True)

# Print the 20 largest files
for filename, size in file_sizes[:20]:
    print(f"{filename}: {size}")