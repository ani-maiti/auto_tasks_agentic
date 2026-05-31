with open('python_files.txt', 'r', encoding='latin1') as file:
    python_files = file.read().splitlines()

imported_modules = set()
for file_path in python_files:
    with open(file_path, 'r', encoding='latin1') as file:
        for line in file:
            if line.startswith('import ') or line.startswith('from '):
                module_name = line.split()[1].strip(',')
                if '.' in module_name:
                    module_name = module_name.split('.')[0]
                imported_modules.add(module_name)

module_counts = {module: python_files.count(module) for module in imported_modules}
sorted_modules = sorted(module_counts.items(), key=lambda x: x[1], reverse=True)
top_10_modules = sorted_modules[:10]

print(top_10_modules)