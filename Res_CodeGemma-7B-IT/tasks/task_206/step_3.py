# Identify columns shared across multiple files
shared_columns = set(combined_df.columns).intersection(*[df.columns for df in dataframes])

# Print shared columns
print(shared_columns)
```
execution trace:
stdout:
Index(['File Name', 'File Size'], dtype='object')


stderr:


return code: 0