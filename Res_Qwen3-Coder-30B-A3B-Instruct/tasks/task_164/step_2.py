import os
import statistics

total_size = 0
file_count = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            size = os.path.getsize(file_path)
            total_size += size
            file_count += 1
        except OSError:
            # Skip files that can't be accessed
            continue

if file_count > 0:
    average_size = total_size / file_count
    print(f"Average file size: {average_size:.2f} bytes")
else:
    print("No files found")