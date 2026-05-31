# Step 2: Identify the file with the most rows
max_rows = 0
file_with_max_rows = None
for file in csv_files:
    df = pd.read_csv(file)
    if df.shape[0] > max_rows:
        max_rows = df.shape[0]
        file_with_max_rows = file
print(f"The file with the most rows is {file_with_max_rows} with {max_rows} rows.")