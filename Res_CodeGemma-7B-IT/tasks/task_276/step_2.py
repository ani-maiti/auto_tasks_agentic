import os

# Get a list of all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Print the list of CSV files
print(csv_files)