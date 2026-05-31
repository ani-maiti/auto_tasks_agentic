import os
import json
import ast

# Find all Python files in the current directory tree
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

# Extract functions, classes, imports, and docstrings from Python files
inventory = {}
for file_path in python_files:
    with open(file_path, 'r') as file:
        content = file.read()
        tree = ast.parse(content)
        
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        imports = [alias.name for alias in ast.walk(tree) if isinstance(alias, ast.alias)]
        docstrings = [ast.get_docstring(node) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef)]
        
        inventory[file_path] = {
            'functions': functions,
            'classes': classes,
            'imports': imports,
            'docstrings': docstrings
        }
print("Inventory built successfully.")