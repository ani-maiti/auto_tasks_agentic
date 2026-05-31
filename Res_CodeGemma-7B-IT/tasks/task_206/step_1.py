import glob
import pandas as pd

# Get all CSV files in the current directory
csv_files = glob.glob("*.csv")

# List to store dataframes for each file
dataframes = []

# Iterate through files and read dataframes
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine dataframes into a single dataframe
combined_df = pd.concat(dataframes, ignore_index=True)

# Get column names from the combined dataframe
column_names = combined_df.columns.tolist()

# Print column names
print(column_names)

# Save column names to a JSON file
combined_df.to_json("combined_schema.json", orient="columns")