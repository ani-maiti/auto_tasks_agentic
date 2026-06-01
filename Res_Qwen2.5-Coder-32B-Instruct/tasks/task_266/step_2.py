import os
import ast

def find_python_files(root):
    return [os.path.join(dp, f) for dp, dn, fn in os.walk(root) for f in fn if f.endswith('.py')]

def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read(), filename=file_path)
    return node

def extract_classes(node):
    classes = {}
    for node in ast.walk(node):
        if isinstance(node, ast.ClassDef):
            bases = [base.id for base in node.bases if isinstance(base, ast.Name)]
            classes[node.name] = {'bases': bases}
    return classes

def build_hierarchy(classes):
    hierarchy = {}
    for cls, info in classes.items():
        hierarchy[cls] = info['bases']
    return hierarchy

def main():
    root_dir = '.'
    python_files = find_python_files(root_dir)
    all_classes = {}

    for file_path in python_files:
        try:
            tree = parse_file(file_path)
            classes = extract_classes(tree)
            all_classes.update(classes)
        except Exception as e:
            print(f"Failed to parse {file_path}: {e}")

    hierarchy = build_hierarchy(all_classes)
    import json
    with open('class_hierarchy.json', 'w') as f:
        json.dump(hierarchy, f, indent=4)

if __name__ == "__main__":
    main()