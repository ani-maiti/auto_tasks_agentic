import os
import glob
import pandas as pd

# Step 1: Discover all CSV files in the current directory
csv_files = glob.glob('*.csv')
print(f"Found {len(csv_files)} CSV files.")

# Step 2: Identify columns containing dates in each CSV file
date_columns = {}
for file in csv_files:
    df = pd.read_csv(file)
    potential_dates = [col for col in df.columns if 'date' in col.lower()]
    date_columns[file] = potential_dates
print(date_columns)