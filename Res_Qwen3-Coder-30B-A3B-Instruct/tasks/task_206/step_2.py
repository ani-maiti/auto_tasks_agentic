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

print(json.dumps(schemas, indent=2))