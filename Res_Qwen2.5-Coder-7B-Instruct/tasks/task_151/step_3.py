import os

# List all directories and files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filter out non-Python files
python_files = [f for f in files if f.endswith('.py')]

if not python_files:
    print("No Python files found.")
else:
    # Count the number of blank lines in each Python file
    total_blank_lines = sum(1 for filename in python_files for line in open(filename) if line.strip() == '')

    print(f"Total blank lines across all Python files: {total_blank_lines}")