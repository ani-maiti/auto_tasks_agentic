with open('csv_files.txt', 'r') as f:
    csv_files = f.read().splitlines()

print(f"Found {len(csv_files)} CSV files.")