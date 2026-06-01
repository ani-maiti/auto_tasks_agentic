import os
import pandas as pd

csv_files = [
    './archive_inventory.csv',
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './largest_cities.csv',
    './common_keys_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './archive_comparison.csv',
    './email_columns_report.csv',
    './results.csv',
    './domain_analysis.csv',
    './metrics_results.csv',
    './report.csv',
    './image_hashes.csv'
]

key_quality_report = {}

for file in csv_files:
    df = pd.read_csv(file)
    report = {}
    for column in df.columns:
        unique_count = df[column].nunique()
        total_count = len(df)
        if total_count == 0:
            uniqueness = 0
            stability = 0
        else:
            uniqueness = unique_count / total_count
            stability = 1.0 if uniqueness == 1 else 0.0
        report[column] = {'uniqueness': uniqueness, 'stability': stability}
    key_quality_report[file] = report

print("Key quality report generated.")