import pandas as pd
import os

csv_files = ['./cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv', './python_files_line_counts.csv', './largest_files.csv', './report.csv']
missing_value_report = {}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        missing_values = df.isnull().sum()
        total_values = df.size
        missing_percentages = (missing_values / total_values) * 100
        missing_value_report[file] = missing_percentages.to_dict()
    except pd.errors.EmptyDataError:
        print(f"File {file} is empty.")
        missing_value_report[file] = {}

print("Missing value percentages by column:")
for file, percentages in missing_value_report.items():
    print(f"File: {file}")
    for column, percentage in percentages.items():
        print(f"  Column: {column}, Missing: {percentage:.2f}%")

worst_column = min((col for file in missing_value_report for col in missing_value_report[file]), key=lambda x: missing_value_report[x.split(',')[0]][x.split(',')[1]], default=None)

if worst_column:
    worst_file, worst_col = worst_column.split(',')
    worst_percentage = missing_value_report[worst_file][worst_col]
    print(f"\nWorst column: {worst_col} in file {worst_file} with {worst_percentage:.2f}% missing values")
else:
    print("\nNo missing values found.")

with open('quality_report.txt', 'w') as f:
    f.write("Quality Report:\n")
    for file, percentages in missing_value_report.items():
        f.write(f"File: {file}\n")
        for column, percentage in percentages.items():
            f.write(f"  Column: {column}, Missing: {percentage:.2f}%\n")
    if worst_column:
        f.write(f"\nWorst column: {worst_col} in file {worst_file} with {worst_percentage:.2f}% missing values\n")
    else:
        f.write("\nNo missing values found.\n")