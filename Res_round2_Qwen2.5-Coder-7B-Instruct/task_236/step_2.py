import json

# Load the first JSON file to get an idea of its structure
with open(json_files[0], 'r') as file:
    sample_json = json.load(file)

# Extract the base name without extension for similarity check
base_name = os.path.splitext(json_files[0])[0]

# Initialize a dictionary to store schemas
schemas = {}

# Loop through all JSON files to collect their schemas
for json_file in json_files:
    if base_name in json_file:
        with open(json_file, 'r') as file:
            data = json.load(file)
            schemas[json_file] = data

# Print collected schemas for verification
for key, value in schemas.items():
    print(f"{key}:")
    print(json.dumps(value, indent=4))