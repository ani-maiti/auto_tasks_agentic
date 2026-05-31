import os
import json

# Find all Python files in the current directory tree
python_files = [f for f in os.walk('.') if f[1] == [] and f[0].endswith('.py')]
print(f"Found {len(python_files)} Python files.")