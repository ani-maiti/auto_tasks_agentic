import os
import ast
import json
from collections import defaultdict

# Get all Python files in the current directory
python_files = [f for f in os.listdir('.') if f.endswith('.py')]

# Initialize data structures
function_complexity = {}
file_complexity = defaultdict(list)

# Iterate over files
for file_name in python_files:
    # Open file and parse AST
    with open(file_name, 'r') as f:
        tree = ast.parse(f.read())

    # Calculate function complexity
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_complexity[node.name] = ast.complexity(node)

    # Calculate file complexity metrics
    file_complexity[file_name] = {
        'lines_of_code': len(tree.body),
        'number_of_functions': len(function_complexity),
        'cyclomatic_complexity': sum(function_complexity.values())
    }

# Save complexity metrics to JSON
with open('complexity.json', 'w') as f:
    json.dump(file_complexity, f, indent=4)

# Generate report
print("Cyclomatic complexity report:")
for file_name, metrics in file_complexity.items():
    print(f"{file_name}:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

# Print most complex file
most_complex_file = max(file_complexity, key=lambda k: file_complexity[k]['cyclomatic_complexity'])
print(f"\nMost complex file: {most_complex_file}")