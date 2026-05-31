import os
import glob
import pandas as pd

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')

print(f"Found {len(csv_files)} CSV files.")

# Function to check if a file has any data
def has_data(file_path):
    try:
        df = pd.read_csv(file_path, nrows=1)
        return not df.empty
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

# Filter out empty files
non_empty_csv_files = [file for file in csv_files if has_data(file)]

print(f"{len(non_empty_csv_files)} non-empty CSV files found.")

# Iterate over each CSV file and identify date columns
all_date_columns = []

for file_path in non_empty_csv_files:
    df = pd.read_csv(file_path)
    date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()
    all_date_columns.extend(date_columns)

unique_date_columns = list(set(all_date_columns))

print(f"Unique date columns found across all CSV files: {unique_date_columns}")