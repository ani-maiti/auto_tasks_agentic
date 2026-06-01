import os
import pandas as pd
from dateutil import parser

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './common_keys_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './archive_comparison.csv',
    './email_columns_report.csv',
    './results.csv',
    './domain_analysis.csv',
    './report.csv',
    './image_hashes.csv'
]

date_columns = {}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        potential_dates = []
        for col in df.columns:
            try:
                pd.to_datetime(df[col], errors='raise')
                potential_dates.append(col)
            except ValueError:
                pass
        if potential_dates:
            date_columns[file] = potential_dates
    except Exception as e:
        print(f"Error reading {file}: {e}")

print(date_columns)