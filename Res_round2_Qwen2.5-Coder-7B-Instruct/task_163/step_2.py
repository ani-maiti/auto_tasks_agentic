import os

files = []
for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        file_path = os.path.join(root, filename)
        if os.path.getsize(file_path) < 100:
            files.append(file_path)

print(files)