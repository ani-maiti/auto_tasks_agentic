import os
import csv

csv_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.csv'):
            csv_files.append(os.path.join(root, file))

print(f"Number of CSV files: {len(csv_files)}")

row_counts = {}
for csv_file in csv_files:
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        row_count = sum(1 for row in reader)
        row_counts[csv_file] = row_count

for file, count in row_counts.items():
    print(f"{file}: {count} rows")