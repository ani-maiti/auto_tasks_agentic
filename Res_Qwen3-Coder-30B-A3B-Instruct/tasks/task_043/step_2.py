import csv
import os

# Get the CSV file path
csv_file = "./largest_files.csv"

# Count rows in the CSV file
row_count = 0
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        row_count += 1

print(f"Number of CSV files: 1")
print(f"Rows in largest_files.csv: {row_count}")