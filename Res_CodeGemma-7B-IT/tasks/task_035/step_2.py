# Print the size of each file
for filename in large_files:
    print(filename, os.path.getsize(filename))