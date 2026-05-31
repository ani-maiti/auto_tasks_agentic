import os
import json

def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

directory_to_search = input("Enter the directory to search for JSON files: ")
json_files = find_json_files(directory_to_search)

if json_files:
    print("JSON files found:")
    for file in json_files:
        print(file)
else:
    print("No JSON files found.")