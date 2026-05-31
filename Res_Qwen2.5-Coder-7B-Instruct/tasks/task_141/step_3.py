import os

# List all files in the current directory and its subdirectories
all_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            all_files.append(os.path.join(root, file))

class_count = 0

# Iterate over each Python file and count the number of classes
for file_path in all_files:
    with open(file_path, 'r') as file:
        content = file.read()
        class_count += content.count('class ')

print(f"Total number of classes defined across all Python files: {class_count}")