import os

max_size = 0
max_file = None

for root, _, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        if file_size > max_size:
            max_size = file_size
            max_file = file_path

print(max_file)