import os
import re
import json

# Get all files in the current directory
files = os.listdir('.')

# Filter files to include only Python files
python_files = [f for f in files if f.endswith('.py')]

# Initialize an empty list to store imported modules
imported_modules = []

# Iterate over each Python file
for file in python_files:
    # Open the file and read its contents
    with open(file, 'r') as f:
        code = f.read()

    # Use regular expressions to extract imported modules
    matches = re.findall(r'import\s+(\w+)', code)
    imported_modules.extend(matches)

# Create a frequency table of imported modules
module_counts = {}
for module in imported_modules:
    module_counts[module] = module_counts.get(module, 0) + 1

# Sort the modules by frequency in descending order
sorted_modules = sorted(module_counts.items(), key=lambda x: x[1], reverse=True)

# Print the ten most common modules
print(json.dumps(sorted_modules[:10]))