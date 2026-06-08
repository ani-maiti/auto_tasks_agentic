import os
import ast

def count_functions_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        tree = ast.parse(content)
        
        function_count = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_count += 1
        
        return function_count
    except Exception as e:
        return 0

total_functions = 0
file_count = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            file_count += 1
            total_functions += count_functions_in_file(file_path)

print(f"Total Python files: {file_count}")
print(f"Total functions: {total_functions}")