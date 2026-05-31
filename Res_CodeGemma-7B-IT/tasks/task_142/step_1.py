import os

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.py'):
            with open(os.path.join(root, filename), 'r') as f:
                num_imports = 0
                for line in f:
                    if line.startswith('import'):
                        num_imports += 1
                print(f'File: {filename}, Imports: {num_imports}')