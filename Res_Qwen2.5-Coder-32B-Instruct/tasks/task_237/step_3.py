import os
import ast

def find_python_files(directory):
    return [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith('.py')]

def is_recursive_function(node):
    if isinstance(node, ast.FunctionDef):
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Name) and child.func.id == node.name:
                return True
    return False

def find_recursive_functions_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=file_path)
        return [node.name for node in ast.walk(tree) if is_recursive_function(node)]
    except SyntaxError:
        return []

def main():
    py_files = find_python_files('.')
    recursive_functions = {}
    for file in py_files:
        functions = find_recursive_functions_in_file(file)
        if functions:
            recursive_functions[file] = functions
    return recursive_functions

recursive_functions = main()
print("Recursive functions found:")
for file, functions in recursive_functions.items():
    print(f"File: {file}, Functions: {functions}")