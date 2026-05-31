import os

total_size = 0
num_files = 0

for root, _, files in os.walk('.'):
    for filename in files:
        file_path = os.path.join(root, filename)
        total_size += os.path.getsize(file_path)
        num_files += 1

average_size = total_size / num_files

print(average_size)