import os
import ast
import networkx as nx

def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py'):
                file_paths.append(os.path.join(root, filename))
    return file_paths

def get_function_calls(file_path):
    with open(file_path, 'r') as f:
        source_code = f.read()
    tree = ast.parse(source_code)
    function_calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            function_calls.append(node.func.id)
    return function_calls

def build_call_graph(file_paths):
    call_graph = nx.DiGraph()
    for file_path in file_paths:
        function_calls = get_function_calls(file_path)
        for caller in function_calls:
            for callee in function_calls:
                if caller != callee:
                    call_graph.add_edge(caller, callee)
    return call_graph

def save_graph_to_json(graph, file_path):
    nx.write_graphml(graph, file_path)

def find_most_called_function(graph):
    function_counts = {}
    for node in graph.nodes:
        function_counts[node] = graph.in_degree(node)
    most_called_function = max(function_counts, key=function_counts.get)
    return most_called_function

# Set the directory to analyze
directory = '/path/to/your/directory'

# Get file paths for all Python files in the directory
file_paths = get_file_paths(directory)

# Build the call graph
call_graph = build_call_graph(file_paths)

# Save the call graph to a JSON file
save_graph_to_json(call_graph, 'call_graph.graphml')

# Find the most frequently called function
most_called_function = find_most_called_function(call_graph)

# Print the most called function
print(f'Most called function: {most_called_function}')