import os
import json

file_list = []

for filename in os.listdir("."):
    if filename.endswith(".py"):
        file_size = os.path.getsize(filename)
        file_list.append({"filename": filename, "size": file_size})

with open("file_list.json", "w") as f:
    json.dump(file_list, f)