import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

# Read all CSV files
csv_files = []
file_data = {}

for file_path in ['./company_mentions.csv', './crypto_prices.csv', './top_python_repos.csv', './long_functions_report.csv', './python_files_line_counts.csv', './largest_files.csv', './config_report.csv', './file_size_histogram.csv', './repo_metadata.csv', './key_analysis.csv', './table_report.csv']:
    try:
        df = pd.read_csv(file_path)
        csv_files.append(file_path)
        file_data[file_path] = {
            'columns': list(df.columns),
            'shape': df.shape,
            'dtypes': df.dtypes.astype(str).to_dict()
        }
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

print("CSV files found:", len(csv_files))