import ast
import json
from collections import Counter
import os

# Find all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

print(f"Found {len(python_files)} Python files")

# Parse files and collect imports
all_imports = []

for file_path in python_files[:10]:  # Process first 10 files for testing
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    all_imports.append(alias.name.split('.')[0])  # Get base module name
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    all_imports.append(node.module.split('.')[0])  # Get base module name
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Collected {len(all_imports)} imports")
print("First 20 imports:", all_imports[:20])