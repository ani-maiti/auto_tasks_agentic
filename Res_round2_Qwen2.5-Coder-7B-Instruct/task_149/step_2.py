import os
import csv

# Define the directory to search for Python files
directory = '.'

# Initialize a list to store file names and their line counts
file_line_counts = []

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            try:
                # Open the file and count the lines
                with open(file_path, 'r', encoding='latin1') as f:
                    line_count = sum(1 for _ in f)
                file_line_counts.append((file_path, line_count))
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Write the results to a CSV file
with open('python_files_line_counts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Path', 'Line Count'])
    writer.writerows(file_line_counts)

print("CSV file generated successfully.")