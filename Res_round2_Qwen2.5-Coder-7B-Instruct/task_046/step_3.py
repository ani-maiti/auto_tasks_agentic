import os

# List all Python files in the current directory
python_files = [f for f in os.listdir('.') if f.endswith('.py')]

if len(python_files) == 0:
    print("No Python files found in the current directory.")
else:
    with open(python_files[0], 'r') as file:
        content = file.read()

    # Count the number of function definitions
    function_count = content.count('def ')

    print(f"Total number of functions defined: {function_count}")