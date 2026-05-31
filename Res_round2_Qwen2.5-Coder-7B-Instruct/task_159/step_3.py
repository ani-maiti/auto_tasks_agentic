import os

def find_zero_byte_files(directory):
    zero_byte_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:
                zero_byte_files.append(file_path)
    return zero_byte_files

directory_to_search = "/path/to/search"  # Replace with the actual directory you want to search
zero_byte_files = find_zero_byte_files(directory_to_search)

if zero_byte_files:
    print("Zero-byte files found:")
    for file in zero_byte_files:
        print(file)
else:
    print("No zero-byte files found.")

# If no zero-byte files were found, try another directory
if not zero_byte_files:
    print("Trying another directory...")
    alternative_directory = "/another/path/to/search"  # Replace with the alternative directory
    zero_byte_files = find_zero_byte_files(alternative_directory)

    if zero_byte_files:
        print("Zero-byte files found in the alternative directory:")
        for file in zero_byte_files:
            print(file)
    else:
        print("No zero-byte files found in the alternative directory.")