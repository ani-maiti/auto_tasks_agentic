import os

def get_file_list(dir_path):
    file_list = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list

def get_function_names(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    function_names = []
    for line in code.splitlines():
        if line.startswith('def '):
            function_name = line.split('(')[0].split()[-1]
            function_names.append(function_name)
    return function_names

def is_recursive_function(function_name, code):
    lines = code.splitlines()
    for i, line in enumerate(lines):
        if line.startswith('def ' + function_name):
            for j in range(i + 1, len(lines)):
                if 'def ' in lines[j]:
                    return True
    return False

def get_longest_recursive_function(file_path):
    code = open(file_path, 'r').read()
    function_names = get_function_names(file_path)
    longest_function = None
    longest_length = 0
    for function_name in function_names:
        if is_recursive_function(function_name, code):
            lines = code.splitlines()
            for i, line in enumerate(lines):
                if line.startswith('def ' + function_name):
                    start_line = i + 1
            end_line = -1
            for i in range(start_line, len(lines)):
                if lines[i].startswith('def '):
                    end_line = i - 1
                    break
            if end_line != -1:
                function_length = end_line - start_line + 1
                if function_length > longest_length:
                    longest_function = function_name
                    longest_length = function_length
    return longest_function

# Get the directory path from the user
dir_path = input("Enter the directory path: ")

# Get the list of files in the directory
file_list = get_file_list(dir_path)

# Find the longest recursive function
longest_recursive_function = None
longest_length = 0
for file_path in file_list:
    function_name = get_longest_recursive_function(file_path)
    if function_name:
        if longest_length < len(function_name):
            longest_recursive_function = function_name
            longest_length = len(function_name)

# Print the longest recursive function
print("Longest recursive function:", longest_recursive_function)