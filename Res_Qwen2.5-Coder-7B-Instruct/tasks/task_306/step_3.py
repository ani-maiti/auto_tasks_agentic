import os
import json
from collections import defaultdict

def calculate_cyclomatic_complexity(file_path):
    # Placeholder function to calculate cyclomatic complexity
    return 10  # Simplified example value

results = defaultdict(dict)

for file_path in py_files:
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            functions = [line.split()[2] for line in content.split('\n') if line.startswith('def')]
            for func in functions:
                cc = calculate_cyclomatic_complexity(file_path)
                results[file_path][func] = cc

# Save results to JSON
with open('complexity_results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Complexity results saved to complexity_results.json")