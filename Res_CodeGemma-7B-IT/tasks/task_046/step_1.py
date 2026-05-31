import glob

file_list = glob.glob("*.py")

num_functions = 0
for file in file_list:
    with open(file, "r") as f:
        code = f.read()
        num_functions += code.count("def ")

print(num_functions)