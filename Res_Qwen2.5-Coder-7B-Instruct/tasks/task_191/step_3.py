# Filter out directories and keep only files
filtered_files = [f for f in modified_files if os.path.isfile(f)]

# Print the filtered list of modified files
print(filtered_files)