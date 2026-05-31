import os
import csv
from networkx import Graph, connected_components
from collections import defaultdict

def get_csv_files(dir_path):
    """
    Returns a list of CSV files in the given directory tree.
    """
    csv_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def infer_schema(file_path):
    """
    Inferred schema of the given CSV file.
    """
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        schema = {header: str(type(value)) for header, value in zip(headers, next(reader))}
    return schema

def identify_foreign_keys(file_path, schema):
    """
    Identifies potential foreign keys in the given CSV file based on column types and relationships.
    """
    foreign_keys = []
    for header, data_type in schema.items():
        if data_type in ['<class \'int\'>', '<class \'float\'>']:
            for other_header, other_type in schema.items():
                if other_header != header and other_type in ['<class \'int\'>', '<class \'float\'>']:
                    foreign_keys.append((header, other_header))
    return foreign_keys

def build_relationship_graph(csv_files, foreign_keys):
    """
    Builds a graph of relationships between CSV files based on foreign keys.
    """
    graph = Graph()
    for file in csv_files:
        graph.add_node(file)
    for file1, file2 in foreign_keys:
        graph.add_edge(file1, file2)
    return graph

def compute_connected_components(graph):
    """
    Computes the connected components of the given graph.
    """
    connected_components = list(connected_components(graph))
    return connected_components

def generate_schema_report(schemas):
    """
    Generates a report of inferred schemas.
    """
    report = ""
    for file, schema in schemas.items():
        report += f"\nSchema for file '{file}':\n"
        for header, data_type in schema.items():
            report += f"\t{header}: {data_type}\n"
    return report

def save_graph_structure(graph, file_path):
    """
    Saves the graph structure to a JSON file.
    """
    graph_dict = {node: list(neighbors) for node, neighbors in graph.adjacency()}
    with open(file_path, 'w') as f:
        json.dump(graph_dict, f)

def print_largest_connected_component(connected_components):
    """
    Prints the largest connected component.
    """
    largest_component = max(connected_components, key=len)
    print(f"\nLargest connected component:\n")
    for file in largest_component:
        print(f"\t{file}")

# Get CSV files in the current directory tree
csv_files = get_csv_files(".")

# Infer schemas for each CSV file
schemas = {file: infer_schema(file) for file in csv_files}

# Identify potential foreign keys between files
foreign_keys = []
for file in csv_files:
    schema = schemas[file]
    foreign_keys.extend(identify_foreign_keys(file, schema))

# Build a relationship graph based on foreign keys
graph = build_relationship_graph(csv_files, foreign_keys)

# Compute connected components of the graph
connected_components = compute_connected_components(graph)

# Generate a report of inferred schemas
schema_report = generate_schema_report(schemas)

# Save the graph structure to a JSON file
save_graph_structure(graph, "graph.json")

# Print the largest connected component
print_largest_connected_component(connected_components)