with open('json_files.txt', 'r') as f:
    json_files = f.read().splitlines()
print(f"Found {len(json_files)} JSON files.")