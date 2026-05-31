# Step 5: Ensure csv_files is defined before importing pandas
import glob
import pandas as pd

# Step 6: Find all CSV files in the current directory
csv_files = glob.glob('*.csv')
print(f"Found {len(csv_files)} CSV files.")

# Step 7: Load the first CSV file to inspect its structure
if csv_files:
    df = pd.read_csv(csv_files[0])
    print(df.head())
else:
    print("No CSV files found.")