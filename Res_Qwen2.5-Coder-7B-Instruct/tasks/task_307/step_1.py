import os
import json

# Step 1: Discover all JSON files in the current directory
json_files = [f for f in os.listdir('.') if f.endswith('.json')]
print(f"Found {len(json_files)} JSON files.")