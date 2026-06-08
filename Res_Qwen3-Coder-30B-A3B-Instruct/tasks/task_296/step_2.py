import ast
import json
from collections import defaultdict, deque
import os

# Function to extract function calls from Python code
def extract_function_calls(file_path):
    with open(file_path, 'r') as file:
        try:
            tree = ast.parse(file.read())
        except SyntaxError as e:
            print(f"Syntax error in {file_path}: {e}")
            return set()
    
    calls = set()
    
    class CallVisitor(ast.NodeVisitor):
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                calls.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr)
            self.generic_visit(node)
    
    visitor = CallVisitor()
    visitor.visit(tree)
    return calls

# Find all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

print(f"Found {len(python_files)} Python files")

# Build function call graph
call_graph = defaultdict(set)

for file_path in python_files[:10]:  # Limit to first 10 for testing
    print(f"Processing {file_path}")
    calls = extract_function_calls(file_path)
    # For simplicity, we'll just add all calls as edges to a dummy function
    # In a real implementation, we'd need to identify actual function definitions
    for call in calls:
        call_graph['dummy_func'].add(call)

# Save to JSON
with open('call_graph.json', 'w') as f:
    json.dump(dict(call_graph), f)

print("Saved call graph to call_graph.json")