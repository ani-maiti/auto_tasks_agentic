import os
import glob
import pandas as pd

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')

print(f"Found {len(csv_files)} CSV files.")

# Load the first CSV file to check its structure
if csv_files:
    file_path = csv_files[0]
    df = pd.read_csv(file_path)

    # Identify columns containing dates
    date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()

    print(f"Date columns found: {date_columns}")
else:
    print("No CSV files found.")