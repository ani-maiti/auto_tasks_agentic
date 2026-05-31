import os

# List all files in the current directory and its subdirectories
files = []
for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.py'):
            files.append(os.path.join(root, filename))

print(f"Found {len(files)} Python files.")

class_counter = 0

# Iterate over each Python file and count the number of classes
for file_path in files:
    with open(file_path, 'r') as file:
        content = file.read()
        class_counter += content.count('class ')

print(f"Total number of classes defined across all Python files: {class_counter}")