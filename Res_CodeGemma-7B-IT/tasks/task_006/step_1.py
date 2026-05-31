import os

def count_empty_files(directory):
    count = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.getsize(file_path) == 0:
                count += 1
    return count

print(count_empty_files("."))