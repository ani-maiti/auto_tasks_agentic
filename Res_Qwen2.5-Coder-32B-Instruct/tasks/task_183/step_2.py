import csv
import os

csv_files = [
    "./cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv",
    "./python_files_line_counts.csv",
    "./largest_files.csv",
    "./report.csv"
]

for file_path in csv_files:
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        row_count = sum(1 for row in reader)
        print(f"{file_path}: {row_count} rows")