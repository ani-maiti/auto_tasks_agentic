import pandas as pd
import os

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './common_keys_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './results.csv',
    './domain_analysis.csv',
    './report.csv'
]

def detect_primary_key(df):
    potential_keys = []
    for col in df.columns:
        if df[col].is_unique:
            potential_keys.append(col)
    return potential_keys

report_lines = ["# Potential Primary Key Columns Report\n"]

for file in csv_files:
    try:
        df = pd.read_csv(file)
        keys = detect_primary_key(df)
        report_lines.append(f"## File: {file}\n")
        if keys:
            report_lines.append("Potential primary key columns:\n")
            for key in keys:
                report_lines.append(f"- {key}\n")
        else:
            report_lines.append("No unique column found for primary key.\n")
    except Exception as e:
        report_lines.append(f"Error processing file {file}: {str(e)}\n")

with open('primary_key_report.md', 'w') as f:
    f.writelines(report_lines)

print("Report generated: primary_key_report.md")