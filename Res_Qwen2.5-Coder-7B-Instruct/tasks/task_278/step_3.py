import os
import glob

# Step 1: Discover all CSV files in the current directory tree
csv_files = glob.glob('**/*.csv', recursive=True)
print(f"Found {len(csv_files)} CSV files.")

# Step 2: Infer schemas for each CSV file
schemas = {}
for file in csv_files:
    df = pd.read_csv(file, nrows=100)  # Read first 100 rows to infer schema
    schema = str(df.dtypes)
    schemas[file] = schema
print("Schemas inferred for all CSV files.")