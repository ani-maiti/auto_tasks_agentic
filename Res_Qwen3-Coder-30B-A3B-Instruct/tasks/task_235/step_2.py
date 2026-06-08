import pandas as pd
import os

def analyze_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        columns = df.columns.tolist()
        
        # Check for potential primary key candidates
        potential_pks = []
        
        for col in columns:
            # Check if column has unique values
            if df[col].nunique() == len(df):
                potential_pks.append(col)
            # Check if column has mostly unique values (95%+)
            elif df[col].nunique() / len(df) > 0.95:
                potential_pks.append(col)
        
        return {
            'file': file_path,
            'columns': columns,
            'potential_primary_keys': potential_pks
        }
    except Exception as e:
        return {
            'file': file_path,
            'error': str(e)
        }

# Analyze all CSV files
results = []
csv_files = ['./company_mentions.csv', './crypto_prices.csv', './long_functions_report.csv', 
             './python_files_line_counts.csv', './largest_files.csv', './config_report.csv', 
             './file_size_histogram.csv', './repo_metadata.csv', './key_analysis.csv']

for csv_file in csv_files:
    result = analyze_csv_file(csv_file)
    results.append(result)

results