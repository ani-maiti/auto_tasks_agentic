import os

# Get the current directory
cwd = os.getcwd()

# Get a list of all files in the current directory
files = os.listdir(cwd)

# Filter files with the .csv extension
csv_files = [file for file in files if file.endswith('.csv')]

# Print the list of CSV files
print(csv_files)

# Iterate over the CSV files
for csv_file in csv_files:
    # Get the full path to the CSV file
    file_path = os.path.join(cwd, csv_file)

    # Open the CSV file
    with open(file_path, 'r') as f:
        # Read the CSV data
        csv_data = csv.reader(f)

        # Get the number of rows in the CSV file
        row_count = len(list(csv_data))

        # Print the row count for each CSV file
        print(f"{csv_file}: {row_count}")