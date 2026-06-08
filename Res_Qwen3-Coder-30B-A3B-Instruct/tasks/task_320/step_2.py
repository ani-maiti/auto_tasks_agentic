import ast
import json
from collections import defaultdict
from difflib import SequenceMatcher

def get_function_definitions(file_path):
    """Extract function definitions from a Python file."""
    try:
        with open(file_path, 'r') as f:
            tree = ast.parse(f.read())
        
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get the source code of the function
                func_source = ast.get_source_segment(f.read(), node)
                functions.append({
                    'name': node.name,
                    'line_start': node.lineno,
                    'line_end': node.end_lineno if hasattr(node, 'end_lineno') else node.lineno,
                    'source': func_source
                })
        return functions
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return []

def calculate_similarity(func1, func2):
    """Calculate similarity between two function sources."""
    # Normalize whitespace and remove extra spaces for better comparison
    s1 = ' '.join(func1['source'].split())
    s2 = ' '.join(func2['source'].split())
    
    return SequenceMatcher(None, s1, s2).ratio()

def find_duplicate_functions():
    """Find duplicate functions across all Python files."""
    all_functions = []
    
    # Get all Python files
    import subprocess
    result = subprocess.run(['find', '.', '-name', '*.py', '-type', 'f'], 
                          capture_output=True, text=True)
    python_files = result.stdout.strip().split('\n')
    
    # Extract functions from each file
    for file_path in python_files:
        if file_path.strip():
            functions = get_function_definitions(file_path)
            for func in functions:
                func['file'] = file_path
                all_functions.append(func)
    
    # Find duplicates based on structural similarity
    duplicates = []
    similarities = []
    
    for i in range(len(all_functions)):
        for j in range(i + 1, len(all_functions)):
            func1 = all_functions[i]
            func2 = all_functions[j]
            
            # Skip if same file and same function name
            if func1['file'] == func2['file'] and func1['name'] == func2['name']:
                continue
                
            similarity = calculate_similarity(func1, func2)
            
            if similarity > 0.8:  # Threshold for considering as duplicate
                duplicates.append({
                    'func1': {
                        'name': func1['name'],
                        'file': func1['file'],
                        'line_start': func1['line_start'],
                        'line_end': func1['line_end']
                    },
                    'func2': {
                        'name': func2['name'],
                        'file': func2['file'],
                        'line_start': func2['line_start'],
                        'line_end': func2['line_end']
                    },
                    'similarity': similarity
                })
                similarities.append(similarity)
    
    # Sort by similarity (descending)
    duplicates.sort(key=lambda x: x['similarity'], reverse=True)
    
    return duplicates

# Find duplicates
duplicates = find_duplicate_functions()

# Generate report
report = {
    "total_duplicates_found": len(duplicates),
    "duplicate_pairs": duplicates
}

# Save to JSON
with open('deduplication_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Deduplication report saved to deduplication_report.json")
print(f"Found {len(duplicates)} duplicate pairs")

if duplicates:
    most_similar = duplicates[0]
    print("\nMost similar pair:")
    print(f"Function '{most_similar['func1']['name']}' in {most_similar['func1']['file']}")
    print(f"Function '{most_similar['func2']['name']}' in {most_similar['func2']['file']}")
    print(f"Similarity: {most_similar['similarity']:.2f}")
else:
    print("No significant duplicates found.")