class_count = 0

# Iterate over each Python file and count the number of classes
for file_path in all_files:
    with open(file_path, 'r') as file:
        content = file.read()
        class_count += content.count('class ')

print(f"Total number of classes defined across all Python files: {class_count}")