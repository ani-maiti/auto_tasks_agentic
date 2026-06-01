import os
import pandas as pd
from difflib import SequenceMatcher

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './common_keys_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './results.csv',
    './domain_analysis.csv',
    './report.csv'
]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

column_similarity_matrix = {}

for file in csv_files:
    df = pd.read_csv(file)
    columns = df.columns.tolist()
    column_similarity_matrix[file] = {col: {} for col in columns}
    for col1 in columns:
        for col2 in columns:
            if col1 != col2:
                column_similarity_matrix[file][col1][col2] = similar(col1, col2)

print(column_similarity_matrix)