import re

dependencies = {}

for file in py_files:
    try:
        with open(file, 'r') as f:
            content = f.read()
            imports = re.findall(r'import\s+(\w+)', content)
            for imp in imports:
                if imp not in dependencies:
                    dependencies[imp] = set()
                dependencies[imp].add(file)
    except Exception as e:
        print(f"Error reading file {file}: {e}")

# Save dependencies to a file
with open('dependencies.txt', 'w') as f:
    for key, value in dependencies.items():
        f.write(f"{key}: {', '.join(value)}\n")