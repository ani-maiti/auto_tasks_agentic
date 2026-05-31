class_counter = 0

# Iterate over each Python file and count the number of classes
for file_path in files:
    with open(file_path, 'r') as file:
        content = file.read()
        class_counter += content.count('class ')

print(f"Total number of classes defined across all Python files: {class_counter}")