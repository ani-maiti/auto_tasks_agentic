import os
import pandas as pd
from collections import defaultdict

print("Reading CSV files and inferring schemas...")

csv_files = [
    "./cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv",
    "./common_keys_report.csv",
    "./python_files_line_counts.csv",
    "./largest_files.csv",
    "./archive_comparison.csv",
    "./email_columns_report.csv",
    "./results.csv",
    "./domain_analysis.csv",
    "./report.csv",
    "./image_hashes.csv"
]

schemas = {}
for file in csv_files:
    try:
        df = pd.read_csv(file)
        schemas[file] = df.dtypes.to_dict()
    except Exception as e:
        print(f"Error reading {file}: {e}")

print(schemas)