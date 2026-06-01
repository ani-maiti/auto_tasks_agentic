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
            normalized_dates[file][col] = df[col].dropna().min(), df[col].dropna().max()
        except Exception as e:
            print(f"Error normalizing {col} in {file}: {e}")

print(normalized_dates)