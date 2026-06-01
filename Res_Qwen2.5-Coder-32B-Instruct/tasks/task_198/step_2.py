import pandas as pd
import os

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './report.csv'
]

max_rows = 0
file_with_max_rows = None

for file in csv_files:
    try:
        df = pd.read_csv(file)
        if len(df) > max_rows:
            max_rows = len(df)
            file_with_max_rows = file
    except Exception as e:
        print(f"Error reading {file}: {e}")

print(f"File with most rows: {file_with_max_rows}")