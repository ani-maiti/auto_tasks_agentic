# Get the directory to summarize
directory_path = input("Enter the directory path: ")

# Get the file information for all files in the directory
file_info_list = get_directory_files(directory_path)

# Create a JSON object from the file information
file_info_json = json.dumps(file_info_list, indent=4)

# Print the JSON object
print(file_info_json)
```
execution trace:
stdout:
Enter the directory path: /home/user/Documents/
{"files": [{"name": "file1.txt", "size": 12345}, {"name": "file2.py", "size": 67890}, {"name": "file3.jpg", "size": 34567}]}
PROCESS TIMED OUT


stderr:

PROCESS TIMED OUT


return code: TIMEOUT