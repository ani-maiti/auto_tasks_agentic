import os
import glob
import pandas as pd

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')

print(f"Found {len(csv_files)} CSV files.")

# Iterate over each CSV file and identify date columns
all_date_columns = []

for file_path in csv_files:
    df = pd.read_csv(file_path)
    date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()
    all_date_columns.extend(date_columns)

unique_date_columns = list(set(all_date_columns))

print(f"Unique date columns found across all CSV files: {unique_date_columns}")