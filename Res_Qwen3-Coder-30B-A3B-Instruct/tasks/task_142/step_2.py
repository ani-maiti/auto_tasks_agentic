import os
import re

def count_import_statements(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Count lines that start with import or from
            import_lines = re.findall(r'^\s*(?:import|from)\s', content, re.MULTILINE)
            return len(import_lines)
    except Exception as e:
        return 0

# Get list of Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

# Count imports in each file
total_imports = 0
file_import_counts = []

for file_path in python_files:
    count = count_import_statements(file_path)
    total_imports += count
    file_import_counts.append((file_path, count))

# Print results
print(f"Total Python files found: {len(python_files)}")
print(f"Total import statements: {total_imports}")
print("\nImport counts per file:")
for file_path, count in file_import_counts:
    print(f"{file_path}: {count}")