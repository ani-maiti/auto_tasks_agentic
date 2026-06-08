import ast
import json
from collections import defaultdict
import subprocess

# First, let's get the list of Python files again
result = subprocess.run(['find', '.', '-name', '*.py', '-type', 'f'], capture_output=True, text=True)
python_files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexities = []
        
    def visit_FunctionDef(self, node):
        complexity = 1  # Base complexity
        
        # Count conditional statements
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.With)):
                complexity += 1
            elif isinstance(child, ast.Try):
                complexity += 1
                # Count except blocks
                complexity += len(child.handlers)
        
        self.complexities.append({
            'function': node.name,
            'file': getattr(node, 'filename', 'unknown'),
            'complexity': complexity,
            'line': node.lineno
        })
        
        self.generic_visit(node)

def analyze_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        visitor = ComplexityVisitor()
        visitor.visit(tree)
        
        # Add filename to each function
        for func in visitor.complexities:
            func['file'] = filepath
            
        return visitor.complexities
    except Exception as e:
        print(f"Error analyzing {filepath}: {e}")
        return []

# Collect all complexities
all_complexities = []

for file_path in python_files:
    if file_path:
        complexities = analyze_file(file_path)
        all_complexities.extend(complexities)

# Sort by complexity (descending)
all_complexities.sort(key=lambda x: x['complexity'], reverse=True)

# Save to JSON
with open('function_complexities.json', 'w') as f:
    json.dump(all_complexities, f, indent=2)

print(f"Analyzed {len(all_complexities)} functions")