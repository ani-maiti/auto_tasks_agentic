import ast
import json
from collections import defaultdict
from difflib import SequenceMatcher
import os

def get_function_definitions(file_path):
    """Extract function definitions from a Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get the source code of the function
                try:
                    func_source = ast.get_source_segment(content, node)
                    functions.append({
                        'name': node.name,
                        'line_start': node.lineno,
                        'line_end': node.end_lineno if hasattr(node, 'end_lineno') else node.lineno,
                        'source': func_source
                    })
                except:
                    # If we can't get the source segment, just use the function name and line info
                    functions.append({
                        'name': node.name,
                        'line_start': node.lineno,
                        'line_end': node.end_lineno if hasattr(node, 'end_lineno') else node.lineno,
                        'source': f"def {node.name}(...):"
                    })
        return functions
    except Exception as e:
        # print(f"Error parsing {file_path}: {e}")
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
    python_files = [f for f in result.stdout.strip().split('\n') if f.strip()]
    
    print(f"Found {len(python_files)} Python files")
    
    # Extract functions from each file
    parsed_count = 0
    for file_path in python_files:
        if file_path.strip():
            functions = get_function_definitions(file_path)
            for func in functions:
                func['file'] = file_path
                all_functions.append(func)
            parsed_count += 1
            if parsed_count % 50 == 0:
                print(f"Parsed {parsed_count} files...")
    
    print(f"Total functions extracted: {len(all_functions)}")
    
    # Find duplicates based on structural similarity
    duplicates = []
    similarities = []
    
    print("Checking for duplicates...")
    for i in range(len(all_functions)):
        for j in range(i + 1, min(i + 1000, len(all_functions))):  # Limit comparisons for performance
            func1 = all_functions[i]
            func2 = all_functions[j]
            
            # Skip if same file and same function name
            if func1['file'] == func2['file'] and func1['name'] == func2['name']:
                continue
                
            try:
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
            except Exception as e:
                # print(f"Error comparing functions: {e}")
                continue
    
    # Sort by similarity (descending)
    duplicates.sort(key=lambda x: x['similarity'], reverse=True)
    
    return duplicates

# Find duplicates
duplicates = find_duplicate_functions()

# Generate report
report = {
    "total_duplicates_found": len(duplicates),
    "duplicate_pairs": duplicates[:10]  # Only keep top 10 most similar pairs
}

# Save to JSON
with open('deduplication_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Deduplication report saved to deduplication_report.json")
print(f"Found {len(duplicates)} duplicate pairs")

if duplicates:
    most_similar = duplicates[0]
    print("\nMost similar pair:")
    print(f"Function '{most_similar['func1']['name']}' in {most_similar