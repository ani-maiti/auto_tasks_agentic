import glob
import pandas as pd
import hashlib

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')

# Initialize an empty list to store candidate keys
candidate_keys = []

# Iterate over each CSV file
for csv_file in csv_files:
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Get the column names
    columns = df.columns

    # Iterate over each column
    for column in columns:
        # Create a candidate key by concatenating the column name and the first 10 rows of the column
        candidate_key = f"{column}_{df[column].head(10).to_string()}"

        # Calculate the MD5 hash of the candidate key
        key_hash = hashlib.md5(candidate_key.encode()).hexdigest()

        # Add the candidate key and hash to the list
        candidate_keys.append({
            'key': candidate_key,
            'hash': key_hash
        })

# Print the candidate keys
print(candidate_keys)