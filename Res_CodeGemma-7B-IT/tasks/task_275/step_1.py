import os
import ast
import json

def get_file_list(directory):
    """
    Returns a list of all Python files in a directory.
    """
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_list.append(os.path.join(root, file))
    return file_list

def get_cyclomatic_complexity(file_path):
    """
    Returns the cyclomatic complexity estimate for a Python function.
    """
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    complexity = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            complexity += 1
    return complexity

def rank_functions(file_list):
    """
    Ranks Python functions by cyclomatic complexity.
    """
    function_data = []
    for file_path in file_list:
        with open(file_path, 'r') as f:
            code = f.read()
        for function_name in ast.FunctionDef.names(ast.parse(code)):
            complexity = get_cyclomatic_complexity(file_path)
            function_data.append({
                'file': file_path,
                'name': function_name,
                'complexity': complexity
            })
    return sorted(function_data, key=lambda f: f['complexity'], reverse=True)

def save_results(function_data, file_path):
    """
    Saves the function ranking data to a JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(function_data, f, indent=4)

# Example usage:
file_list = get_file_list('.')
function_data = rank_functions(file_list)
save_results(function_data, 'function_ranking.json')