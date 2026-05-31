import os
import json

# Find all Python files in the current directory and its subdirectories
python_files = [f for f in os.walk('.')] if f.endswith('.py')]
print(python_files)