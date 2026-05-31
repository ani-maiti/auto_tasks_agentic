# Identify columns shared across multiple files
shared_columns = set(column_names).intersection(*[df.columns for df in dataframes])

# Print shared columns
print(shared_columns)