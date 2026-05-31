# Filter out directories and keep only files
files_only = [f for f in files if os.path.isfile(f)]

# Print the list of files
print(files_only)