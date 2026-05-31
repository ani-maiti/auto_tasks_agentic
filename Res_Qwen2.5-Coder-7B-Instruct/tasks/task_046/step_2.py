# Read the content of each Python file and count the number of function definitions
function_count = 0

for file_name in python_files:
    with open(file_name, 'r') as file:
        content = file.read()
        # Count the number of function definitions in the file
        function_count += content.count('def ')

print(f"Total number of functions defined across all Python files: {function_count}")