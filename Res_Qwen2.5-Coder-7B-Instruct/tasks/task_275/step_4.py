# Step 2: Filter out non-Python files
python_files = [file for sublist in python_files for file in sublist if file.endswith('.py')]

print(python_files)