import os

# Count JSON files and list their names
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

print(f"Number of JSON files: {len(json_files)}")
print("JSON files:")
for file in json_files:
    print(file)