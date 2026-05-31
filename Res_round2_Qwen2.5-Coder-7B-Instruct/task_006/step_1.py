import os

empty_files_count = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) == 0:
            empty_files_count += 1

print(f"Number of empty files: {empty_files_count}")