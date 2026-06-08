import pandas as pd
import json
from collections import defaultdict

# Read all CSV files and infer schemas
csv_files = ['./python_files_line_counts.csv', './largest_files.csv', './file_size_histogram.csv', './key_analysis.csv']
schemas = {}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        schema = {}
        for col in df.columns:
            schema[col] = str(df[col].dtype)
        schemas[file] = schema
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Find shared columns
all_columns = defaultdict(list)
for file, schema in schemas.items():
    for col in schema.keys():
        all_columns[col].append(file)

shared_columns = {col: files for col, files in all_columns.items() if len(files) > 1}

# Create combined schema report
combined_report = {
    "individual_schemas": schemas,
    "shared_columns": shared_columns,
    "total_files": len(csv_files),
    "total_unique_columns": len(all_columns)
}

# Save to JSON file
with open('schema_report.json', 'w') as f:
    json.dump(combined_report, f, indent=2)

print("Schema report saved to schema_report.json")