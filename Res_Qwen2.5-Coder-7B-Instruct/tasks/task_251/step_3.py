import ast
from collections import defaultdict

def get_function_calls(file_path):
    function_calls = defaultdict(set)
    
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = getattr(node.func, 'id', None)
                if func_name:
                    function_calls[func_name].add(node.lineno)
                    
    return function_calls

all_functions = set()
called_functions = set()

for file_path in python_files:
    function_calls = get_function_calls(file_path)
    all_functions.update(function_calls.keys())
    called_functions.update(function_calls.values())

never_called_functions = all_functions - called_functions

report = {
    "total_functions": len(all_functions),
    "called_functions": len(called_functions),
    "never_called_functions": list(never_called_functions)
}

import json
with open('never_called_functions.json', 'w') as file:
    json.dump(report, file, indent=4)

print("Report saved to never_called_functions.json")