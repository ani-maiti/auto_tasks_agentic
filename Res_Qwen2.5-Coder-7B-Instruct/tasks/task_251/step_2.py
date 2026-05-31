with open('python_files.txt', 'r') as file:
    python_files = file.readlines()

python_files = [file.strip() for file in python_files]
print(python_files)