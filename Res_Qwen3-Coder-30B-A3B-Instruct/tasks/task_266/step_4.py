import ast
import json
from collections import defaultdict
import os

# Function to recursively find Python files
def find_python_files(directory='.'):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

# Find all Python files
python_files = find_python_files()

print(f"Found {len(python_files)} Python files")

# Parse each file to find classes and their inheritance
class_hierarchy = defaultdict(list)

# Let's examine one file to see if we can detect classes properly
test_file = python_files[0] if python_files else None
if test_file:
    print(f"Examining file: {test_file}")
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # Find all class definitions
        classes_found = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                bases = []
                
                # Get base classes
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        bases.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        bases.append(ast.unparse(base))
                
                classes_found.append((class_name, bases))
                class_hierarchy[class_name] = bases
        
        print(f"Classes found in {test_file}: {classes_found}")
        
    except Exception as e:
        print(f"Error processing {test_file}: {e}")

# Now let's process a few more files to get better data
for i, file_path in enumerate(python_files[1:5]):  # Process next 4 files
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
                        bases.append(ast.unparse(base))
                
                class_hierarchy[class_name] = bases
                
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Save to JSON file
with open('class_hierarchy.json', 'w') as f:
    json.dump(dict(class_hierarchy), f, indent=2)

print("Class hierarchy saved to class_hierarchy.json")
print(f"Found {len(class_hierarchy)} classes total")