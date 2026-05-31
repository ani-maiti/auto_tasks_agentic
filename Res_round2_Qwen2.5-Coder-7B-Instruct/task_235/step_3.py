import os
import glob
import pandas as pd

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')
print(f"Found {len(csv_files)} CSV files.")

# Function to detect potential primary key columns
def detect_primary_key_columns(df):
    # Check for unique values and non-null values
    potential_keys = []
    for column in df.columns:
        if df[column].is_unique and df[column].notnull().all():
            potential_keys.append(column)
    return potential_keys

# Process each CSV file and store results
results = {}
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    primary_keys = detect_primary_key_columns(df)
    results[csv_file] = primary_keys

# Print the results
for csv_file, keys in results.items():
    print(f"{csv_file}: Potential primary key columns - {keys}")