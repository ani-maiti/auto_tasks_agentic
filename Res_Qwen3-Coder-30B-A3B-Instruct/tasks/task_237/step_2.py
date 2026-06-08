import ast
import os

class RecursiveFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.recursive_functions = []
        
    def visit_FunctionDef(self, node):
        # Check if this function calls itself
        func_name = node.name
        recursive_calls = []
        
        class CallVisitor(ast.NodeVisitor):
            def __init__(self, func_name):
                self.func_name = func_name
                self.is_recursive = False
                
            def visit_Call(self, call_node):
                if isinstance(call_node.func, ast.Name):
                    if call_node.func.id == self.func_name:
                        self.is_recursive = True
                elif isinstance(call_node.func, ast.Attribute):
                    if isinstance(call_node.func.value, ast.Name) and call_node.func.value.id == 'self':
                        if call_node.func.attr == self.func_name:
                            self.is_recursive = True
                self.generic_visit(call_node)
        
        call_visitor = CallVisitor(func_name)
        call_visitor.visit(node)
        
        if call_visitor.is_recursive:
            # Calculate the number of lines in the function
            start_line = node.lineno
            end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 10  # Default to 10 lines
            line_count = end_line - start_line + 1
            
            self.recursive_functions.append({
                'name': func_name,
                'file': getattr(self, 'current_file', 'unknown'),
                'lines': line_count,
                'start_line': start_line
            })
        
        self.generic_visit(node)

def find_recursive_functions_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        tree = ast.parse(content)
        visitor = RecursiveFunctionVisitor()
        visitor.current_file = file_path
        visitor.visit(tree)
        
        return visitor.recursive_functions
    except Exception as e:
        return []

# Find all Python files and check for recursive functions
all_recursive_functions = []

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            recursive_funcs = find_recursive_functions_in_file(file_path)
            all_recursive_functions.extend(recursive_funcs)

# Sort by line count to find the longest
if all_recursive_functions:
    longest_function = max(all_recursive_functions, key=lambda x: x['lines'])
    print("Longest recursive function:")
    print(f"Name: {longest_function['name']}")
    print(f"File: {longest_function['file']}")
    print(f"Lines: {longest_function['lines']}")
else:
    print("No recursive functions found.")