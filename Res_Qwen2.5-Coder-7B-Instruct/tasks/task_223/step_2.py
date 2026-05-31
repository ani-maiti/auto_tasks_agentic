import pandas as pd

# Step 2: Identify columns containing dates in each CSV file
date_columns = {}
for file in csv_files:
    df = pd.read_csv(file)
    potential_dates = [col for col in df.columns if 'date' in col.lower()]
    date_columns[file] = potential_dates
print(date_columns)