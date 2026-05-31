# Check if the 'extensions' dictionary is empty
if not extensions:
    print("No files found.")
    exit(0)

# Create a list of extensions to sort
extensions_list = list(extensions.keys())

# Sort the extensions alphabetically
extensions_list.sort()

# Print the sorted extension counts
for extension in extensions_list:
    print(f"{extension}: {extensions[extension]}")