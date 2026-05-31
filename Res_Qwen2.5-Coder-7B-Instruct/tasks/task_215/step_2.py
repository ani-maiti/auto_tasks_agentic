# Read the list of CSV files into a Python list
with open('csv_files.txt', 'r') as file:
    csv_files = file.read().splitlines()

print(f"Found {len(csv_files)} CSV files.")