# Step 2: Load the first CSV file to inspect its structure
df = pd.read_csv(csv_files[0])
print(df.head())