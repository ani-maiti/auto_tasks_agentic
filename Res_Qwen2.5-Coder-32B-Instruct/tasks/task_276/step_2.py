import pandas as pd
import os
from itertools import combinations

csv_files = [
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './common_keys_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './archive_comparison.csv',
    './email_columns_report.csv',
    './results.csv',
    './domain_analysis.csv',
    './report.csv',
    './image_hashes.csv'
]

correlation_reports = []

for file in csv_files:
    try:
        df = pd.read_csv(file)
        numeric_df = df.select_dtypes(include=[float, int])
        if len(numeric_df.columns) > 1:
            corr_matrix = numeric_df.corr().abs()
            upper_tri = corr_matrix.where(pd.np.triu(pd.np.ones(corr_matrix.shape), k=1).astype(bool))
            highly_corr_pairs = [(i, j) for i, j in zip(*upper_tri.stack().index) if upper_tri[i, j] > 0.8]
            if highly_corr_pairs:
                report = f"# Correlation Report for {file}\n\n"
                report += "Pairs with correlation > 0.8:\n\n"
                for pair in highly_corr_pairs:
                    report += f"- {pair[0]} and {pair[1]}: {upper_tri[pair[0], pair[1]]:.2f}\n"
                correlation_reports.append(report)
    except Exception as e:
        print(f"Error processing {file}: {e}")

with open('correlation_report.md', 'w') as f:
    for report in correlation_reports:
        f.write(report)

print("Correlation report generated.")