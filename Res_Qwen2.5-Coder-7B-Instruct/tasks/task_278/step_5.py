import pandas as pd

# Step 3: Identify potential foreign key relationships between files
relationships = []
for i, file1 in enumerate(csv_files):
    for j, file2 in enumerate(csv_files):
        if i != j:
            df1 = pd.read_csv(file1, nrows=100)
            df2 = pd.read_csv(file2, nrows=100)
            common_columns = set(df1.columns).intersection(set(df2.columns))
            if len(common_columns) > 0:
                relationships.append((file1, file2, common_columns))

print(f"Identified {len(relationships)} potential foreign key relationships.")