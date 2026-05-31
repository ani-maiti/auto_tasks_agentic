# Ensure csv_files is defined before using it
csv_files = [f.strip() for f in open('csv_files.txt', 'r').readlines()]

max_rows = 0
largest_file = None

for file in csv_files:
    df = pd.read_csv(file)
    if df.shape[0] > max_rows:
        max_rows = df.shape[0]
        largest_file = file

print(f"Largest file: {largest_file} with {max_rows} rows.")