import os
import ast

def get_python_files(directory):
    return [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith('.py')]

def parse_functions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)
    return {node.name: ast.dump(node) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}

python_files = get_python_files('.')
functions_by_file = {file: parse_functions(file) for file in python_files}
print(functions_by_file.keys())