# Filter out directories and files larger than 100 bytes
filtered_files = [file for file in files if os.path.isfile(file) and os.path.getsize(file) < 100]

print(filtered_files)