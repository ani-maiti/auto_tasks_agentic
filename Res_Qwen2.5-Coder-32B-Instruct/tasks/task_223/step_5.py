import os
import pandas as pd
from datetime import datetime

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './common_keys_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './domain_analysis.csv'
]

date_columns = {}
date_ranges = {}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        for col in df.columns:
            try:
                # Try to convert column to datetime, coerce errors to NaT
                date_series = pd.to_datetime(df[col], errors='coerce')
                if date_series.notna().any():  # Check if there are any valid dates
                    if file not in date_columns:
                        date_columns[file] = []
                    date_columns[file].append(col)
                    min_date = date_series.dropna().min()
                    max_date = date_series.dropna().max()
                    date_ranges[(file, col)] = (min_date, max_date)
            except ValueError:
                continue
    except Exception as e:
        print(f"Error reading {file}: {e}")

print("Date columns found:", date_columns)
print("Date ranges:", date_ranges)

# Save report
with open('date_report.txt', 'w') as f:
    f.write("Date columns found:\n")
    for file, cols in date_columns.items():
        f.write(f"{file}: {cols}\n")
    f.write("\nDate ranges:\n")
    for (file, col), (min_date, max_date) in date_ranges.items():
        f.write(f"{file}, {col}: {min_date} to {max_date}\n")

# Find widest date range
widest_range = None
widest_file_col = None
for (file, col), (min_date, max_date) in date_ranges.items():
    range_days = (max_date - min_date).days
    if widest_range is None or range_days > widest_range:
        widest_range = range_days
        widest_file_col = (file, col)

if widest_file_col:
    print(f"Widest date range found: {widest_file_col[0]}, {widest_file_col[1]}: {widest_range} days")
else:
    print("No valid date ranges found.")