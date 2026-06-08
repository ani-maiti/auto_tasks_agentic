import ast
import json
from collections import defaultdict
import sys

# Function to calculate cyclomatic complexity
def calculate_cyclomatic_complexity(node):
    complexity = 1
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.If, ast.While, ast.For, ast.With, ast.ExceptHandler)):
            complexity += 1
        elif isinstance(child, ast.BoolOp):
            complexity += len(child.values) - 1
        complexity += calculate_cyclomatic_complexity(child)
    return complexity

# Function to analyze a Python file
def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        functions = []
        total_complexity = 0
        
        # Find all functions and calculate their complexity
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                complexity = calculate_cyclomatic_complexity(node)
                total_complexity += complexity
                functions.append({
                    'name': node.name,
                    'complexity': complexity,
                    'line_start': node.lineno,
                    'line_end': node.end_lineno if hasattr(node, 'end_lineno') else node.lineno
                })
        
        # Calculate file-level metrics
        total_lines = len(content.split('\n'))
        code_lines = sum(1 for line in content.split('\n') if line.strip() and not line.strip().startswith('#'))
        comment_lines = sum(1 for line in content.split('\n') if line.strip().startswith('#'))
        
        return {
            'file_path': file_path,
            'total_functions': len(functions),
            'total_complexity': total_complexity,
            'average_function_complexity': total_complexity / len(functions) if functions else 0,
            'functions': functions,
            'total_lines': total_lines,
            'code_lines': code_lines,
            'comment_lines': comment_lines
        }
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

# Main analysis function
def main():
    # Find all Python files
    import subprocess
    result = subprocess.run(['find', '.', '-name', '*.py', '-type', 'f'], 
                          capture_output=True, text=True)
    
    python_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
    
    # Analyze each file
    results = []
    for file_path in python_files:
        if file_path:
            analysis = analyze_file(file_path)
            if analysis:
                results.append(analysis)
    
    # Save results to JSON
    with open('complexity_report.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Find the most complex file
    if results:
        most_complex = max(results, key=lambda x: x['total_complexity'])
        print("Most complex file:")
        print(f"File: {most_complex['file_path']}")
        print(f"Total Complexity: {most_complex['total_complexity']}")
        print(f"Average Function Complexity: {most_complex['average_function_complexity']:.2f}")
        print(f"Number of Functions: {most_complex['total_functions']}")
        
        # Print top 5 most complex functions
        print("\nTop 5 most complex functions:")
        all_functions = []
        for file_result in results:
            for func in file_result['functions']:
                all_functions.append({
                    'file': file_result['file_path'],
                    'function': func['name'],
                    'complexity': func['complexity']
                })
        
        sorted_functions = sorted(all_functions, key=lambda x: x['complexity'], reverse=True)[:5]
        for i, func in enumerate(sorted_functions, 1):
            print(f"{i}. {func['file']}:{func['function']} - Complexity: {func['complexity']}")
    
    return results

if __name__ == "__main__":
    results = main()