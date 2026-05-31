import ast

def extract_info(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    functions = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
    classes = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    imports = [alias.name for alias in tree.body if isinstance(alias, ast.Import) or isinstance(alias, ast.ImportFrom)]
    docstrings = [ast.get_docstring(node) for node in tree.body if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef)]
    
    return {
        'file': file_path,
        'functions': functions,
        'classes': classes,
        'imports': imports,
        'docstrings': docstrings
    }

project_inventory = {}
for file in python_files:
    project_inventory[file] = extract_info(file)

print("Project inventory extracted.")