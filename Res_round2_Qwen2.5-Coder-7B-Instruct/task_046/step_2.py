with open(python_files[0], 'r') as file:
    content = file.read()

# Count the number of function definitions
function_count = content.count('def ')

print(f"Total number of functions defined: {function_count}")