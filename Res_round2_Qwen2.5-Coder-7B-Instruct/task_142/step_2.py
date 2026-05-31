import re

total_imports = 0

# Iterate over each file and count import statements
for file_path in files:
    with open(file_path, 'r') as file:
        content = file.read()
        # Use regex to find import statements
        imports = re.findall(r'\bimport\s+\w+(\.\w+)*\b', content)
        total_imports += len(imports)

print(f"Total import statements found: {total_imports}")