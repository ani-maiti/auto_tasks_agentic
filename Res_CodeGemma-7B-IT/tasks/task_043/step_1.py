import os

# Get the current directory
cwd = os.getcwd()

# Get a list of all files in the current directory
files = os.listdir(cwd)

# Filter files ending in '.csv'
csv_files = [f for f in files if f.endswith('.csv')]

# Print the number of CSV files
print(f"Number of CSV files: {len(csv_files)}")

# Print the row counts of each CSV file
for csv_file in csv_files:
    with open(csv_file, 'r') as f:
        rows = f.readlines()
        print(f"{csv_file}: {len(rows)} rows")