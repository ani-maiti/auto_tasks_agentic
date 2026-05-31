import pandas as pd

# Initialize a dictionary to store file names and row counts
row_counts = {}

for file in csv_files:
    df = pd.read_csv(file)
    row_counts[file] = len(df)

print(row_counts)