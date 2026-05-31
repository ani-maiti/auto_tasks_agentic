import ast

def get_function_length(node):
    if isinstance(node, ast.FunctionDef):
        return len(node.body)
    return 0

def analyze_file(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    function_lengths = [(node.name, get_function_length(node)) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return function_lengths

function_lengths = []
for file_path in python_files:
    function_lengths.extend(analyze_file(file_path))

long_functions = [func for func, length in function_lengths if length > 50]
sorted_long_functions = sorted(long_functions, key=lambda x: x[1], reverse=True)

with open('report.csv', 'w') as f:
    f.write("Function Name,File Path,Length\n")
    for func, path, length in sorted_long_functions:
        f.write(f"{func},{path},{length}\n")

top_ten = sorted_long_functions[:10]

print("Top 10 longest functions:")
for func, path, length in top_ten:
    print(f"{func} in {path}: {length} lines")