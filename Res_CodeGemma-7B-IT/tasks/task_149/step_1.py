import os

# Get all Python files in the current directory
python_files = [f for f in os.listdir('.') if f.endswith('.py')]

# Create a list of lists to store the file names and line counts
data = []

# Iterate through the Python files and count the lines
for file in python_files:
    with open(file) as f:
        data.append([file, len(f.readlines())])

# Write the data to a CSV file
with open('python_files.csv', 'w') as f:
    for file_name, line_count in data:
        f.write(f"{file_name},{line_count}\n")