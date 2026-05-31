import os

# Get all files in the current directory
files = os.listdir('.')

# Filter files to include only Python files
python_files = [f for f in files if f.endswith('.py')]

# Get the line count for each Python file
line_counts = [len(open(f).readlines()) for f in python_files]

# Sort files by line count in descending order
sorted_files = sorted(zip(python_files, line_counts), key=lambda x: x[1], reverse=True)

# Print the top 10 longest files by line count
for file, count in sorted_files[:10]:
    print(f"{file}: {count} lines")