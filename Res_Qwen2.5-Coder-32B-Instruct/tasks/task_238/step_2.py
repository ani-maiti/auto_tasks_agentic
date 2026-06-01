import os
import ast
from collections import defaultdict

def get_python_files(directory):
    return [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith('.py')]

def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)
    return tree

def extract_functions(tree):
    functions = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions[node.name] = node.lineno
    return functions

def extract_calls(tree, functions):
    calls = defaultdict(list)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in functions:
                calls[node.func.id].append(node.lineno)
    return calls

def build_call_graph(files):
    call_graph = defaultdict(lambda: defaultdict(list))
    for file in files:
        tree = parse_file(file)
        functions = extract_functions(tree)
        calls = extract_calls(tree, functions)
        for func, call_lines in calls.items():
            for line in call_lines:
                call_graph[file][func].append(line)
    return call_graph

def save_graph_to_json(graph, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(graph, f, indent=4)

def find_most_frequent_function(graph):
    from collections import Counter
    all_calls = []
    for file_calls in graph.values():
        for func_calls in file_calls.values():
            all_calls.extend(func_calls)
    counter = Counter(all_calls)
    most_common = counter.most_common(1)
    return most_common[0] if most_common else None

files = get_python_files('.')
call_graph = build_call_graph(files)
save_graph_to_json(call_graph, 'call_graph.json')
most_frequent = find_most_frequent_function(call_graph)
print(f"Most frequently called function: {most_frequent}")