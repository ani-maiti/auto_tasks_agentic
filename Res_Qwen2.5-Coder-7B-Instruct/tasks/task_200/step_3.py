with open('imports.txt', 'r') as f:
    imports = f.read().splitlines()

unique_imports = set(imports)
print(unique_imports)