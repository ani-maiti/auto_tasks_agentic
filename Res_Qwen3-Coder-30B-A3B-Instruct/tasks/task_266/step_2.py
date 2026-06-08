import ast
import json
from collections import defaultdict

# Find all Python files
import subprocess
result = subprocess.run(['find', '.', '-name', '*.py', '-type', 'f'], capture_output=True, text=True)
python_files = result.stdout.strip().split('\n') if result.stdout.strip() else []

# Filter out empty strings
python_files = [f for f in python_files if f]

print(f"Found {len(python_files)} Python files")

# Parse each file to find classes and their inheritance
class_hierarchy = defaultdict(list)

for file_path in python_files[:5]:  # Process first 5 files for testing
    if not file_path:
        continue
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # Find all class definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                bases = []
                
                # Get base classes
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        bases.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        bases.append(ast.unparse(base))  # Python 3.9+
                
                class_hierarchy[class_name] = bases
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(json.dumps(dict(class_hierarchy), indent=2))