import ast
import json
from collections import defaultdict, Counter

# Create a graph to store function calls
call_graph = defaultdict(list)
function_counts = Counter()

# Process each Python file
for file_path in [line.strip() for line in open('/dev/stdin') if line.strip()]:
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Parse the Python file into an AST
        tree = ast.parse(content)
        
        # Extract function definitions
        function_names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_names.add(node.name)
        
        # Find function calls
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                func_name = node.func.id
                # Only count calls to functions defined in this file
                if func_name in function_names:
                    function_counts[func_name] += 1
                    # Add to call graph (we'll add caller info later)
    except Exception as e:
        pass  # Skip files that can't be parsed

# Convert to JSON format
graph_data = {
    "functions": dict(function_counts),
    "most_frequent": function_counts.most_common(1)[0] if function_counts else None
}

print(json.dumps(graph_data, indent=2))