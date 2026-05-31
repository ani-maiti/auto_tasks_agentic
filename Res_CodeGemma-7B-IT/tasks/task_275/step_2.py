def get_function_names(tree):
    """
    Returns a list of function names from an AST tree.
    """
    function_names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_names.append(node.name)
    return function_names

# Update rank_functions to use get_function_names:
def rank_functions(file_list):
    """
    Ranks Python functions by cyclomatic complexity.
    """
    function_data = []
    for file_path in file_list:
        with open(file_path, 'r') as f:
            code = f.read()
        tree = ast.parse(code)
        function_names = get_function_names(tree)
        for function_name in function_names:
            complexity = get_cyclomatic_complexity(file_path)
            function_data.append({
                'file': file_path,
                'name': function_name,
                'complexity': complexity
            })
    return sorted(function_data, key=lambda f: f['complexity'], reverse=True)