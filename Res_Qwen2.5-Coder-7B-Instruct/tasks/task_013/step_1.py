import os
import re

def count_imports(directory):
    total_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    count = len(re.findall(r'\bimport\b', content))
                    total_count += count
    return total_count

print(count_imports('.'))