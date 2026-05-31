# Step 2: Identify columns containing dates in each CSV file
date_columns = {}
for file in csv_files:
    df = pd.read_csv(file)
    date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    date_columns[file] = date_cols
print("Date columns identified:")
for file, cols in date_columns.items():
    print(f"{file}: {cols}")