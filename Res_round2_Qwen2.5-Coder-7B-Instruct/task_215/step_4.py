import os
import glob
import pandas as pd

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')

# Check if there are any CSV files
if len(csv_files) == 0:
    print("No CSV files found in the current directory.")
else:
    # Load the first CSV file to check if it's valid
    df = pd.read_csv(csv_files[0])
    print("Loaded CSV file:", csv_files[0])