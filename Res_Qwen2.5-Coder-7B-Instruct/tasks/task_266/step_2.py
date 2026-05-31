# Step 2: Identify classes and inheritance relationships in the discovered Python files.
class_info = {}

def extract_class_info(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        exec(content, globals(), locals())
        for name, obj in locals().items():
            if isinstance(obj, type):
                class_info[name] = {
                    'file': file_path,
                    'base_classes': [b.__name__ for b in obj.__bases__]
                }

for file in python_files:
    extract_class_info(file)

print(f"Extracted info for {len(class_info)} classes.")