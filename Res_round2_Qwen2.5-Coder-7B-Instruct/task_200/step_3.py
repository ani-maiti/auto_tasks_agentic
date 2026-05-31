import re

dependencies = {}

for file in py_files:
    with open(file, 'r') as f:
        content = f.read()
        imports = re.findall(r'import\s+(\w+)', content)
        for imp in imports:
            if imp not in dependencies:
                dependencies[imp] = set()
            dependencies[imp].add(file)

# Save dependencies to a file
with open('dependencies.txt', 'w') as f:
    for key, value in dependencies.items():
        f.write(f"{key}: {', '.join(value)}\n")
```

This script reads each Python file, extracts the import statements, and builds a dictionary where keys are module names and values are sets of files that import those modules. It then saves this information to a file named `dependencies.txt`.