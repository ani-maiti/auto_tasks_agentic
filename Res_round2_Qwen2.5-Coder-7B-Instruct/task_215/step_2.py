import pandas as pd

# Load the first CSV file to check if it's valid
df = pd.read_csv(csv_files[0])
print("Loaded CSV file:", csv_files[0])