import os

total_size = 0
file_count = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        total_size += os.path.getsize(file_path)
        file_count += 1

if file_count > 0:
    average_size = total_size / file_count
    print(f"Average file size: {average_size} bytes")
else:
    print("No files found.")