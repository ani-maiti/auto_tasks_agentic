import os

def get_dir_size(directory):
    total_size = 0
    for entry in os.scandir(directory):
        if entry.is_file():
            total_size += entry.stat().st_size
        elif entry.is_dir():
            total_size += get_dir_size(entry.path)
    return total_size

def find_largest_directory(root_directory):
    largest_dir = None
    largest_size = 0

    for directory in os.listdir(root_directory):
        path = os.path.join(root_directory, directory)
        if os.path.isdir(path):
            size = get_dir_size(path)
            if size > largest_size:
                largest_size = size
                largest_dir = directory

    return largest_dir

# Example usage:
root_directory = "/path/to/root/directory"
largest_dir = find_largest_directory(root_directory)

print(f"The largest directory is: {largest_dir}")