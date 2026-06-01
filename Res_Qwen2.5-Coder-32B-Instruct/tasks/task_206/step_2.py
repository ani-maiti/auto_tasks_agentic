import pandas as pd
import json
from collections import defaultdict

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './report.csv'
]

schema_report = defaultdict(list)

for file in csv_files:
    try:
        df = pd.read_csv(file)
        schema = df.dtypes.to_dict()
        for column, dtype in schema.items():
            if column not in schema_report:
                schema_report[column] = []
            schema_report[column].append((file, str(dtype)))
    except Exception as e:
        print(f"Error reading {file}: {e}")

shared_columns = {col: files for col, files in schema_report.items() if len(files) > 1}

with open('combined_schema_report.json', 'w') as f:
    json.dump(shared_columns, f, indent=4)

print("Combined schema report generated and saved to combined_schema_report.json")