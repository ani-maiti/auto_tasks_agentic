import pandas as pd
import json
from collections import defaultdict

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './python_files_line_counts.csv',
    './largest_files.csv'
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

# Generate a more detailed report including individual file schemas
detailed_schema_report = {file: {} for file in csv_files}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        schema = df.dtypes.to_dict()
        detailed_schema_report[file] = {col: str(dtype) for col, dtype in schema.items()}
    except Exception as e:
        print(f"Error reading {file}: {e}")

with open('detailed_combined_schema_report.json', 'w') as f:
    json.dump(detailed_schema_report, f, indent=4)

print("Detailed combined schema report generated and saved to detailed_combined_schema_report.json")