import os
import re
import csv
from collections import namedtuple

FunctionInfo = namedtuple('FunctionInfo', ['file_path', 'function_name', 'line_count'])

def find_long_functions(directory):
    long_functions = []
    
    # Find all Python files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find function definitions
                function_pattern = r'def\s+(\w+)\s*\([^)]*\):'
                function_matches = list(re.finditer(function_pattern, content))
                
                # Get line numbers for each function
                lines = content.split('\n')
                for i, match in enumerate(function_matches):
                    func_name = match.group(1)
                    start_line = match.start()
                    
                    # Find where this function ends
                    end_line = len(lines)
                    if i + 1 < len(function_matches):
                        end_line = function_matches[i+1].start()
                    
                    # Count lines in function body
                    func_lines = lines[match.end():end_line]
                    line_count = len([l for l in func_lines if l.strip() != ''])
                    
                    if line_count > 50:
                        long_functions.append(FunctionInfo(file_path, func_name, line_count))
    
    return long_functions

# Find all long functions
long_functions = find_long_functions('.')

# Sort by line count (descending)
long_functions.sort(key=lambda x: x.line_count, reverse=True)

# Save to CSV
with open('long_functions_report.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Path', 'Function Name', 'Line Count'])
    for func in long_functions:
        writer.writerow([func.file_path, func.function_name, func.line_count])

# Print top 10
print("Top 10 longest functions:")
for i, func in enumerate(long_functions[:10]):
    print(f"{i+1}. {func.file_path}:{func.function_name} ({func.line_count} lines)")