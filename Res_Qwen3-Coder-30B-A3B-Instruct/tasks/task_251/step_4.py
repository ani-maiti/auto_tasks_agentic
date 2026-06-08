import ast
import json
from collections import defaultdict

# Dictionary to store all function definitions and their call sites
function_definitions = defaultdict(list)
function_calls = defaultdict(list)

# Read the file list
with open('python_files.txt', 'r') as f:
    file_paths = [line.strip() for line in f if line.strip()]

# Process each Python file to extract function definitions and calls
for file_path in file_paths:
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # Extract function definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_definitions[file_path].append(node.name)
            
            # Extract function calls
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                function_calls[file_path].append(node.func.id)
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Find unused functions
unused_functions = {}

for file_path, functions in function_definitions.items():
    used_functions = set(function_calls[file_path])
    unused = [func for func in functions if func not in used_functions]
    
    if unused:
        unused_functions[file_path] = unused

# Save results to JSON
with open('unused_functions_report.json', 'w') as f:
    json.dump(unused_functions, f, indent=2)

print("Report generated successfully.")