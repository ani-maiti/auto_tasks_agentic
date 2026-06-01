import json
import glob

json_files = glob.glob('**/*.json', recursive=True)
print(f"Found {len(json_files)} JSON files.")