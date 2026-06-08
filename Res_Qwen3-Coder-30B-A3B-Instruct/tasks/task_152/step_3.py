import os
import subprocess

def count_comment_lines():
    # Find all Python files
    result = subprocess.run(['find', '.', '-name', '*.py', '-type', 'f'], 
                          capture_output=True, text=True)
    
    if result.returncode != 0:
        return 0
    
    files = result.stdout.strip().split('\n')
    total_comments = 0
    
    # Count comments in each file
    for file_path in files:
        if file_path.strip() == '':
            continue
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                comment_count = sum(1 for line in lines if line.strip().startswith('#'))
                total_comments += comment_count
        except Exception:
            # Skip files that can't be read
            continue
    
    return total_comments

print(count_comment_lines())