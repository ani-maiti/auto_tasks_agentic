import os
import json

for filename in os.listdir("."):
    if filename.endswith(".json"):
        try:
            with open(filename) as f:
                json.load(f)
            print(f"{filename}: valid")
        except json.JSONDecodeError:
            print(f"{filename}: invalid")