import os
import json
from typing import Any, Dict, List, Tuple

def get_json_files(directory: str) -> List[str]:
    """
    Get a list of all JSON files in the given directory.

    Args:
        directory: The directory to search.

    Returns:
        A list of file paths for all JSON files in the directory.
    """
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files

def get_schema(json_file: str) -> Dict[str, Any]:
    """
    Get the schema of a JSON file.

    Args:
        json_file: The file path of the JSON file.

    Returns:
        The schema of the JSON file.
    """
    with open(json_file, "r") as f:
        json_data = json.load(f)
    return json_data

def get_common_structural_patterns(json_files: List[str]) -> Dict[str, List[str]]:
    """
    Get the common structural patterns in the given JSON files.

    Args:
        json_files: A list of file paths for JSON files.

    Returns:
        A dictionary of common structural patterns to file paths.
    """
    schemas = [get_schema(file) for file in json_files]
    common_patterns = {}
    for schema in schemas:
        for key, value in schema.items():
            if key not in common_patterns:
                common_patterns[key] = []
            common_patterns[key].append(value)
    return common_patterns

def cluster_files_by_schema_similarity(json_files: List[str], common_patterns: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Cluster files by schema similarity.

    Args:
        json_files: A list of file paths for JSON files.
        common_patterns: A dictionary of common structural patterns to file paths.

    Returns:
        A dictionary of clusters of file paths, where each key is a cluster label and each value is a list of file paths.
    """
    clusters = {}
    for file in json_files:
        schema = get_schema(file)
        cluster_label = None
        for key, values in common_patterns.items():
            if schema.get(key) in values:
                cluster_label = key
                break
        if cluster_label not in clusters:
            clusters[cluster_label] = []
        clusters[cluster_label].append(file)
    return clusters

def generate_report(clusters: Dict[str, List[str]]) -> str:
    """
    Generate a report describing each cluster.

    Args:
        clusters: A dictionary of clusters of file paths.

    Returns:
        A report describing each cluster.
    """
    report = ""
    for cluster_label, files in clusters.items():
        report += f"Cluster {cluster_label}:\n"
        for file in files:
            report += f"- {file}\n"
        report += "\n"
    return report

def save_results(clusters: Dict[str, List[str]], output_file: str):
    """
    Save the results to JSON.

    Args:
        clusters: A dictionary of clusters of file paths.
        output_file: The file path to save the results to.
    """
    with open(output_file, "w") as f:
        json.dump(clusters, f)

def print_largest_cluster(clusters: Dict[str, List[str]]):
    """
    Print the largest cluster.

    Args:
        clusters: A dictionary of clusters of file paths.
    """
    largest_cluster = max(clusters.items(), key=lambda x: len(x[1]))
    print(f"Largest cluster: {largest_cluster[0]}")
    for file in largest_cluster[1]:
        print(f"- {file}")

# Get the current directory.
current_directory = os.getcwd()

# Get a list of all JSON files in the current directory tree.
json_files = get_json_files(current_directory)

# Get the common structural patterns in the JSON files.
common_patterns = get_common_structural