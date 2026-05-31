import os

# List all Python files in the current directory
python_files = [f for f in os.listdir('.') if f.endswith('.py')]

# Initialize the function count
function_count = 0

# Read the content of each Python file and count the number of function definitions
for file_name in python_files:
    with open(file_name, 'r') as file:
        content = file.read()
        # Count the number of function definitions in the file
        function_count += content.count('def ')

print(f"Total number of functions defined across all Python files: {function_count}")