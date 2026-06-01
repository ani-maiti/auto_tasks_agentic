import os
import glob
import json
from radon.complexity import cc_visit

def find_python_files(directory):
    return glob.glob(os.path.join(directory, '**', '*.py'), recursive=True)

def calculate_complexity(file_paths):
    complexities = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            source = file.read()
            results = cc_visit(source)
            for result in results:
                complexities.append({
                    'file': file_path,
                    'function': result.name,
                    'complexity': result.complexity
                })
    return complexities

def main():
    directory = '.'
    file_paths = find_python_files(directory)
    complexities = calculate_complexity(file_paths)
    complexities.sort(key=lambda x: x['complexity'], reverse=True)
    with open('complexity_results.json', 'w') as f:
        json.dump(complexities, f, indent=4)

main()