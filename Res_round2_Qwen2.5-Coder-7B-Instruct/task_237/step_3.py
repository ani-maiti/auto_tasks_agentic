# Step 2: Identify recursive functions in each Python file
def is_recursive_function(func_def):
    return 'def' in func_def and 'return' in func_def and '(' in func_def and ')' in func_def

def extract_functions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        functions = [line.strip() for line in content.split('\n') if line.strip().startswith('def')]
    return functions

recursive_functions = []

for file_path in python_files:
    functions = extract_functions(file_path)
    for func in functions:
        if is_recursive_function(func):
            recursive_functions.append((file_path, func))

print(f"Identified {len(recursive_functions)} recursive functions across {len(set([func[0] for func in recursive_functions]))} files.")