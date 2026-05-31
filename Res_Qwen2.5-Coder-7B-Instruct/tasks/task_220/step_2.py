with open('python_files.txt', 'r') as f:
    files = f.read().splitlines()

imported_modules = set()
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        for line in content.split('\n'):
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                module = line.split()[1].strip(',')
                if '.' in module:
                    module = module.split('.')[0]
                imported_modules.add(module)

print(imported_modules)