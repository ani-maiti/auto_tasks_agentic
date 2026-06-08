import csv
import os

# Create a list to store file info
file_info = []

# Find all Python files and count lines
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_count = sum(1 for line in f)
                file_info.append((file_path, line_count))
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Write to CSV file
with open('python_files_line_counts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Path', 'Line Count'])
    writer.writerows(file_info)

print("CSV file 'python_files_line_counts.csv' has been created.")