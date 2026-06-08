import os
import ast

def has_async_function(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.async_:
                return True
        return False
    except Exception:
        return False

python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

async_files = []
for file in python_files:
    if has_async_function(file):
        async_files.append(file)

print("Python files with async functions:")
for file in async_files:
    print(file)