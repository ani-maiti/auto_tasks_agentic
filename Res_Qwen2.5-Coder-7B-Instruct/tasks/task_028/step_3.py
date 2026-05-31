import pandas as pd

# Read the list of files into a DataFrame
df = pd.read_csv('largest_files.txt', delimiter='\s+', skiprows=1)

# Rename columns for clarity
df.columns = ['size', 'link_dest', 'file']

# Save the DataFrame to a CSV file
df.to_csv('100_largest_files.csv', index=False)