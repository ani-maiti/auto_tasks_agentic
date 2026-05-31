import pandas as pd
from collections import defaultdict

# Read all CSV files into DataFrames
csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './file_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './python_files_line_counts_sorted.csv',
    './file_sizes.csv'
]

dataframes = [pd.read_csv(file) for file in csv_files]

# Infer schemas
schemas = [df.dtypes.to_dict() for df in dataframes]

# Identify common columns
common_columns = set(dataframes[0].columns)
for df in dataframes[1:]:
    common_columns.intersection_update(df.columns)

print("Common Columns:", common_columns)

# Generate combined schema report
combined_schema = {}
for i, schema in enumerate(schemas):
    for col, dtype in schema.items():
        if col not in combined_schema:
            combined_schema[col] = {'dtype': dtype, 'files': []}
        combined_schema[col]['files'].append(csv_files[i])

# Save to JSON
with open('combined_schema.json', 'w') as f:
    json.dump(combined_schema, f, indent=4)

print("Combined schema saved to combined_schema.json")