import pandas as pd

# Step 2: Infer schemas for each CSV file
schemas = {}
for file in csv_files:
    df = pd.read_csv(file, nrows=100)  # Read first 100 rows to infer schema
    schema = str(df.dtypes)
    schemas[file] = schema
print("Schemas inferred for all CSV files.")