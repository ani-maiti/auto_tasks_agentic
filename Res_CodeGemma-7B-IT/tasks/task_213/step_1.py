import os
import re

def find_long_functions(directory):
    """
    Finds all Python files in a directory and detects functions longer than 50 lines.

    Args:
        directory: The directory to search.

    Returns:
        A list of tuples containing the filename and the list of long functions in that file.
    """
    long_functions = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(os.path.join(directory, filename), "r") as f:
                code = f.read()
            functions = re.findall(r"def\s+(\w+)\(.*?\):", code)
            for function in functions:
                function_lines = code.count("\n", code.index(f"def {function}("), code.index("\n", code.index(f"def {function}(") + 1))
                if function_lines > 50:
                    long_functions.append((filename, function))
    return long_functions

def generate_csv(long_functions):
    """
    Generates a CSV report of long functions.

    Args:
        long_functions: A list of tuples containing the filename and the list of long functions in that file.
    """
    with open("long_functions.csv", "w") as f:
        f.write("Filename,Function\n")
        for filename, functions in long_functions:
            for function in functions:
                f.write(f"{filename},{function}\n")

def print_top_ten(long_functions):
    """
    Prints the top ten long functions.

    Args:
        long_functions: A list of tuples containing the filename and the list of long functions in that file.
    """
    sorted_functions = sorted(long_functions, key=lambda x: len(x[1]), reverse=True)
    for i, (filename, functions) in enumerate(sorted_functions[:10]):
        print(f"{i+1}. {filename}: {functions}")

# Find all long functions in the current directory
long_functions = find_long_functions(".")

# Generate a CSV report
generate_csv(long_functions)

# Print the top ten long functions
print_top_ten(long_functions)