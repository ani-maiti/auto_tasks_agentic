import pandas as pd

# Define the list of CSV files again
csv_files = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv']

# Load the first CSV file to check if it's valid
df = pd.read_csv(csv_files[0])
print("Loaded CSV file:", csv_files[0])