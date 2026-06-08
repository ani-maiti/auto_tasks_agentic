import os
import ast
import json
from collections import defaultdict

def analyze_python_file(file_path):
    """Analyze a Python file and extract functions, classes, imports, and docstrings."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        result = {
            'file_path': file_path,
            'functions': [],
            'classes': [],
            'imports': [],
            'total_items': 0,
            'documented_items': 0
        }
        
        # Extract imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    result['imports'].append(f"import {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    result['imports'].append(f"from {module} import {alias.name}")
        
        # Extract functions and classes
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = {
                    'name': node.name,
                    'docstring': ast.get_docstring(node),
                    'line_number': node.lineno
                }
                result['functions'].append(func_info)
                result['total_items'] += 1
                if func_info['docstring']:
                    result['documented_items'] += 1
                    
            elif isinstance(node, ast.ClassDef):
                class_info = {
                    'name': node.name,
                    'docstring': ast.get_docstring(node),
                    'line_number': node.lineno,
                    'methods': []
                }
                result['classes'].append(class_info)
                result['total_items'] += 1
                if class_info['docstring']:
                    result['documented_items'] += 1
                
                # Extract methods from classes
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_info = {
                            'name': item.name,
                            'docstring': ast.get_docstring(item),
                            'line_number': item.lineno
                        }
                        class_info['methods'].append(method_info)
                        result['total_items'] += 1
                        if method_info['docstring']:
                            result['documented_items'] += 1
        
        return result
    
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

# Find all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

print(f"Found {len(python_files)} Python files")

# Analyze each file
inventory = []
undocumented_functions = []

for file_path in python_files:
    analysis = analyze_python_file(file_path)
    if analysis:
        inventory.append(analysis)
        
        # Find undocumented functions
        for func in analysis['functions']:
            if not func['docstring']:
                undocumented_functions.append({
                    'file': file_path,
                    'function': func['name'],
                    'line': func['line_number']
                })

# Generate documentation coverage report
coverage_report = []
for item in inventory:
    if item['total_items'] > 0:
        coverage = (item['documented_items'] / item['total_items']) * 100
    else:
        coverage = 100.0  # No items to document, so 100% coverage
    
    coverage_report.append({
        'file': item['file_path'],
        'coverage_percentage': round(coverage, 2),
        'total_items': item['total_items'],
        'documented_items': item['documented_items']
    })

# Sort by coverage percentage
coverage_report.sort(key=lambda x: x['coverage_percentage'])

# Save to JSON
with open('documentation_coverage.json', 'w') as f:
    json.dump({
        'inventory': inventory,
        'coverage_report': coverage_report,
        'undocumented_functions': undocumented_functions
    }, f, indent=2)

# Print files with lowest coverage
print("\nFiles with lowest documentation coverage:")
for item in coverage_report[:5]:  # Top 5 worst covered
    print(f"{item['file']}: {item['coverage_percentage']}% ({item['documented_items']}/{item['total_items']})")