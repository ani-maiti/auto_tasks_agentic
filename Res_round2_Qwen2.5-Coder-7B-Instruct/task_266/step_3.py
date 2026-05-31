# Step 2: Read the content of each Python file and extract class definitions
class_definitions = {}
for file_path in python_files:
    with open(file_path, 'r') as file:
        content = file.read()
        exec(content, globals(), locals())
        for name, obj in locals().items():
            if inspect.isclass(obj):
                class_definitions[name] = obj.__module__

print(f"Extracted {len(class_definitions)} class definitions.")