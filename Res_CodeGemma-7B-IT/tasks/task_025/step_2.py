# Get the directory to summarize
directory_path = input("Enter the directory path: ")

# Get the file information for all files in the directory
file_info_list = get_directory_files(directory_path)

# Create a JSON object from the file information
file_info_json = json.dumps(file_info_list, indent=4)

# Print the JSON object
print(file_info_json)