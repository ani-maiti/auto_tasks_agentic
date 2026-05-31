import os
import json

def get_file_size(file_path):
  """
  Returns the size of a file in bytes.
  """
  return os.path.getsize(file_path)

def get_file_info(file_path):
  """
  Returns a dictionary of file information for a given file path.
  """
  file_info = {
    "name": os.path.basename(file_path),
    "size": get_file_size(file_path),
  }
  return file_info

def get_directory_files(directory_path):
  """
  Returns a list of dictionaries of file information for all files in a directory.
  """
  file_info_list = []
  for root, _, files in os.walk(directory_path):
    for file_name in files:
      file_path = os.path.join(root, file_name)
      file_info_list.append(get_file_info(file_path))
  return file_info_list

# Get the directory to summarize
directory_path = input("Enter the directory path: ")

# Get the file information for all files in the directory
file_info_list = get_directory_files(directory_path)

# Create a JSON object from the file information
file_info_json = json.dumps(file_info_list, indent=4)

# Print the JSON object
print(file_info_json)