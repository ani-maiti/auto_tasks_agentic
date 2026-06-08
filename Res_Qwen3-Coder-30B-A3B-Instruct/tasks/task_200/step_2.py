import ast
import os
from collections import defaultdict, Counter
import graphviz

# Find all Python files
python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

print(f"Found {len(python_files)} Python files")

# Parse imports from each file
file_imports = defaultdict(list)
module_counts = Counter()

for file_path in python_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module_counts[alias.name] += 1
                    file_imports[file_path].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    module_counts[node.module] += 1
                    file_imports[file_path].append(node.module)
                    
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")

print(f"Found {len(module_counts)} unique modules imported")
print("Top 10 most imported modules:")
for module, count in module_counts.most_common(10):
    print(f"  {module}: {count}")

# Create Graphviz graph
dot = graphviz.Digraph(comment='Python Dependency Graph')
dot.attr(rankdir='LR')

# Add nodes and edges
for file_path, imports in file_imports.items():
    # Normalize file path for display
    file_label = os.path.relpath(file_path)
    dot.node(file_label, file_label, shape='box')
    
    for imp in imports:
        # Create a node for the imported module
        dot.node(imp, imp, shape='ellipse')
        # Create an edge from file to imported module
        dot.edge(file_label, imp)

# Save the graph
dot.render('python_dependencies', format='dot', cleanup=True)
print("Graph saved as python_dependencies.dot")

# Generate report
report_lines = [
    "Python Dependency Report",
    "=" * 30,
    f"Total Python files analyzed: {len(python_files)}",
    f"Total unique modules imported: {len(module_counts)}",
    "",
    "Top 10 Most Imported Modules:",
]

for module, count in module_counts.most_common(10):
    report_lines.append(f"{module}: {count}")

report_content = "\n".join(report_lines)

with open('dependency_report.txt', 'w') as f:
    f.write(report_content)

print("Report saved as dependency_report.txt")