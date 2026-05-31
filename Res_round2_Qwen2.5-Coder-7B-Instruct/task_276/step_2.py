import pandas as pd
import numpy as np

# Function to calculate correlation matrix
def calculate_correlation(file_path):
    df = pd.read_csv(file_path)
    corr_matrix = df.corr()
    return corr_matrix

# List of CSV files found
csv_files = [
    './crypto_prices.csv',
    './hacker_news_stories.csv',
    './cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv',
    './file_report.csv',
    './release_age_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './python_files_line_counts_sorted.csv',
    './duplicate_images.csv',
    './timestamp_stats.csv',
    './sample_headers.csv',
    './image_urls.csv',
    './report.csv',
    './file_sizes.csv',
    './analysis.csv',
    './common_image_dimensions.csv'
]

# Dictionary to store correlation matrices
correlation_matrices = {}

for file in csv_files:
    try:
        corr_matrix = calculate_correlation(file)
        correlation_matrices[file] = corr_matrix
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Print the first few rows of the correlation matrix for the first file
print(correlation_matrices[csv_files[0]].head())
```

This script finds all CSV files in the current directory and its subdirectories, calculates the correlation matrix for each file, and stores them in a dictionary. It then prints the first few rows of the correlation matrix for the first file.