# Step 2: Load all JSON files into a list of dictionaries
data_list = []
for file in json_files:
    with open(file, 'r') as f:
        data_list.append(json.load(f))
print("All JSON files loaded successfully.")