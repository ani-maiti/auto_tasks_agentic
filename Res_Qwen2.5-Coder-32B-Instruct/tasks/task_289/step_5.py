import os
import pandas as pd
from dateutil import parser

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './python_files_line_counts.csv',
    './results.csv',
    './domain_analysis.csv'
]

date_columns = {}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        potential_dates = []
        for col in df.columns:
            try:
                pd.to_datetime(df[col], errors='coerce').dropna()
                potential_dates.append(col)
            except ValueError:
                pass
        if potential_dates:
            date_columns[file] = potential_dates
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Normalize date formats
normalized_dates = {}

for file, cols in date_columns.items():
    df = pd.read_csv(file)
    normalized_dates[file] = {}
    for col in cols:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            non_na_dates = df[col].dropna()
            if not non_na_dates.empty:
                normalized_dates[file][col] = non_na_dates.min(), non_na_dates.max()
        except Exception as e:
            print(f"Error normalizing {col} in {file}: {e}")

# Detect overlapping datasets
overlaps = {}

for file1, cols1 in normalized_dates.items():
    overlaps[file1] = {}
    for col1, (min1, max1) in cols1.items():
        for file2, cols2 in normalized_dates.items():
            if file1 != file2:
                for col2, (min2, max2) in cols2.items():
                    if min1 <= max2 and min2 <= max1:
                        overlaps[file1][f"{file2} ({col2})"] = (max(min1, min2), min(max1, max2))

print(overlaps)

# Save the analysis to JSON
import json

with open('date_analysis.json', 'w') as f:
    json.dump({'date_columns': date_columns, 'normalized_dates': normalized_dates, 'overlaps': overlaps}, f)

# Generate a report
report = []

for file, cols in normalized_dates.items():
    report.append(f"File: {file}")
    for col, (min_date, max_date) in cols.items():
        report.append(f"  Column: {col}, Range: {min_date} to {max_date}")

for file1, overlaps_info in overlaps.items():
    report.append(f"Overlaps for {file1}:")
    for file2_col, overlap_range in overlaps_info.items():
        report.append(f"  Overlaps with {file2_col}: {overlap_range[0]} to {overlap_range[1]}")

report_text = "\n".join(report)

with open('date_analysis_report.txt', 'w') as f:
    f.write(report_text)

# Print the dataset with the widest range
widest_range = None
widest_file = None
widest_col = None

for file, cols in normalized_dates.items():
    for col, (min_date, max_date) in cols.items():
        if min_date is not pd.NaT and max_date is not pd.NaT:
            range_days = (max_date - min_date).days
            if widest_range is None or range_days > widest_range:
                widest_range = range_days
                widest_file = file
                widest_col = col

if widest_file:
    print(f"The dataset with the widest range is {widest_file}, column {widest_col} with a range of {widest_range} days.")
else:
    print("No valid date ranges found.")