import pandas as pd
import numpy as np
from collections import defaultdict

# Initialize data structure to store results
all_results = {}

# Process each CSV file
for csv_file in ['./long_functions_report.csv', './python_files_line_counts.csv', './largest_files.csv', './file_size_histogram.csv', './key_analysis.csv']:
    try:
        df = pd.read_csv(csv_file)
        missing_values = df.isnull().sum()
        total_rows = len(df)
        
        # Calculate percentage of missing values per column
        missing_percentages = (missing_values / total_rows) * 100
        
        # Store results
        all_results[csv_file] = {
            'missing_values': missing_values,
            'missing_percentages': missing_percentages
        }
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

# Save quality report
with open('quality_report.txt', 'w') as f:
    for file_name, data in all_results.items():
        f.write(f"File: {file_name}\n")
        f.write("Missing Values by Column:\n")
        for col, count in data['missing_values'].items():
            f.write(f"  {col}: {count} ({data['missing_percentages'][col]:.2f}%)\n")
        f.write("\n")

# Find worst column across all files
worst_column = None
max_percentage = -1

for file_name, data in all_results.items():
    for col, percentage in data['missing_percentages'].items():
        if percentage > max_percentage:
            max_percentage = percentage
            worst_column = col

print(worst_column)