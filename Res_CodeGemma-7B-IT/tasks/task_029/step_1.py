import os

def count_lines(dir_path):
    total_lines = 0
    for filename in os.listdir(dir_path):
        if filename.endswith('.sh'):
            with open(os.path.join(dir_path, filename), 'r') as f:
                total_lines += len(f.readlines())
    return total_lines

# Replace with the actual directory path
directory_path = '/path/to/directory'

# Run the function and print the result
num_lines = count_lines(directory_path)
print("Total lines:", num_lines)