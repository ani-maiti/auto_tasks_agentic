import pandas as pd
import os

# Find the CSV with the most rows
csv_files = ['./python_files_line_counts.csv', './largest_files.csv', './file_size_histogram.csv']
max_rows = 0
largest_file = None

for file in csv_files:
    try:
        df = pd.read_csv(file)
        row_count = len(df)
        if row_count > max_rows:
            max_rows = row_count
            largest_file = file
    except Exception as e:
        print(f"Error reading {file}: {e}")

print(f"Largest file: {largest_file} with {max_rows} rows")
```