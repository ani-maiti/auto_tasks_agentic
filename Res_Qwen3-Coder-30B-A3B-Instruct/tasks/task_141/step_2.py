import os
import re

def count_classes_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Pattern to match class definitions
        class_pattern = r'^\s*class\s+[A-Za-z_][A-Za-z0-9_]*\s*(:|\(.*\):)'
        classes = re.findall(class_pattern, content, re.MULTILINE)
        return len(classes)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

# Get list of Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

# Count classes in each file
total_classes = 0
for file_path in python_files:
    class_count = count_classes_in_file(file_path)
    total_classes += class_count
    print(f"{file_path}: {class_count} classes")

print(f"\nTotal classes found: {total_classes}")