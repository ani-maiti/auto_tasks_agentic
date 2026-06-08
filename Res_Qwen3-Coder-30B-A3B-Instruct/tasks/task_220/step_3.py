import ast
import json
from collections import Counter
import os

# Find all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

print(f"Found {len(python_files)} Python files")

# Parse files and collect imports
all_imports = []

for file_path in python_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module_name = alias.name.split('.')[0]
                    # Filter out standard library modules
                    if module_name not in ['os', 'json', 'sys', 'io', 're', 'collections', 'functools', 'itertools', 'operator', 'abc', 'contextlib', 'dataclasses', 'enum', 'heapq', 'keyword', 'numbers', 'operator', 'pathlib', 'pickle', 'reprlib', 'statistics', 'struct', 'typing', 'urllib', 'warnings', 'weakref', 'bisect', 'copy', 'csv', 'email', 'html', 'http', 'inspect', 'logging', 'math', 'multiprocessing', 'platform', 'pprint', 'queue', 'sched', 'secrets', 'shutil', 'signal', 'smtplib', 'socket', 'sqlite3', 'ssl', 'string', 'tabulate', 'threading', 'time', 'tracemalloc', 'types', 'typing', 'unittest', 'uuid', 'zipfile']:
                        all_imports.append(module_name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    module_name = node.module.split('.')[0]
                    # Filter out standard library modules
                    if module_name not in ['os', 'json', 'sys', 'io', 're', 'collections', 'functools', 'itertools', 'operator', 'abc', 'contextlib', 'dataclasses', 'enum', 'heapq', 'keyword', 'numbers', 'operator', 'pathlib', 'pickle', 'reprlib', 'statistics', 'struct', 'typing', 'urllib', 'warnings', 'weakref', 'bisect', 'copy', 'csv', 'email', 'html', 'http', 'inspect', 'logging', 'math', 'multiprocessing', 'platform', 'pprint', 'queue', 'sched', 'secrets', 'shutil', 'signal', 'smtplib', 'socket', 'sqlite3', 'ssl', 'string', 'tabulate', 'threading', 'time', 'tracemalloc', 'types', 'typing', 'unittest', 'uuid', 'zipfile']:
                        all_imports.append(module_name)
    
    except Exception as e:
        pass

# Generate frequency table
import_counter = Counter(all_imports)
print("Top 10 most common third-party modules:")
for module, count in import_counter.most_common(10):
    print(f"{module}: {count}")

# Save to JSON
with open('module_frequency.json', 'w') as f:
    json.dump(dict(import_counter), f)

print("\nFrequency table saved to module_frequency.json")