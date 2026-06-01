import pandas as pd
import json
import os
from scipy.stats import zscore, iqr

csv_files = [
    './archive_inventory.csv',
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './largest_cities.csv',
    './common_keys_report.csv',
    './timeline.csv',
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

outlier_results = {}

for file in csv_files:
    try:
        df = pd.read_csv(file)
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) == 0:
            continue
        
        file_outliers = {}
        for col in numeric_cols:
            data = df[col].dropna()
            if len(data) < 2:
                continue
            
            z_scores = zscore(data)
            iqr_scores = (data < (data.quantile(0.25) - 1.5 * iqr(data))) | (data > (data.quantile(0.75) + 1.5 * iqr(data)))
            
            z_outliers = (abs(z_scores) > 3).sum()
            iqr_outliers = iqr_scores.sum()
            
            file_outliers[col] = {
                'z_score_outliers': z_outliers,
                'iqr_outliers': iqr_outliers,
                'total_outliers': z_outliers + iqr_outliers,
                'outlier_ratio': (z_outliers + iqr_outliers) / len(data) if not data.empty else 0
            }
        
        outlier_results[file] = file_outliers
    except Exception as e:
        print(f"Failed to process {file}: {e}")

with open('outlier_results.json', 'w') as f:
    json.dump(outlier_results, f, indent=4)

print("Outlier detection complete. Results saved to outlier_results.json")