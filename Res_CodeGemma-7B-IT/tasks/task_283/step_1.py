import os
import re
import json
from collections import defaultdict

# Get the current directory
current_dir = os.getcwd()

# Create a dictionary to store the project inventory
project_inventory = defaultdict(list)

# Function to extract functions, classes, imports, and docstrings from a file
def extract_code_elements(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    functions = re.findall(r"def\s+(\w+)\(.*?\):", code)
    classes = re.findall(r"class\s+(\w+)\(.*?\):", code)
    imports = re.findall(r"import\s+(\w+)", code)
    docstrings = re.findall(r'"""(.*?)"""', code, re.DOTALL)

    return functions, classes, imports, docstrings

# Function to build the project inventory
def build_inventory(current_dir):
    for root, _, files in os.walk(current_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".py"):
                functions, classes, imports, docstrings = extract_code_elements(file_path)
                project_inventory[file_path].extend(functions)
                project_inventory[file_path].extend(classes)
                project_inventory[file_path].extend(imports)
                project_inventory[file_path].extend(docstrings)

# Function to identify undocumented functions
def identify_undocumented_functions(functions):
    undocumented_functions = []
    for function in functions:
        if not project_inventory[file_path][function]:
            undocumented_functions.append(function)
    return undocumented_functions

# Function to generate a documentation coverage report
def generate_coverage_report(functions):
    coverage_report = {}
    for function in functions:
        coverage_report[function] = bool(project_inventory[file_path][function])
    return coverage_report

# Function to save the project inventory to JSON
def save_inventory(project_inventory):
    with open("project_inventory.json", "w") as f:
        json.dump(project_inventory, f)

# Function to print the files with the lowest coverage
def print_lowest_coverage_files(coverage_reports):
    lowest_coverage_files = []
    for file_path, coverage_report in coverage_reports.items():
        if not coverage_report:
            lowest_coverage_files.append(file_path)
    print("Files with the lowest coverage:")
    for file_path in lowest_coverage_files:
        print(file_path)

# Build the project inventory
build_inventory(current_dir)

# Identify undocumented functions
undocumented_functions = []
for file_path, functions in project_inventory.items():
    undocumented_functions.extend(identify_undocumented_functions(functions))

# Generate documentation coverage report
coverage_reports = {}
for file_path, functions in project_inventory.items():
    coverage_reports[file_path] = generate_coverage_report(functions)

# Save the project inventory to JSON
save_inventory(project_inventory)

# Print the files with the lowest coverage
print_lowest_coverage_files(coverage_reports)