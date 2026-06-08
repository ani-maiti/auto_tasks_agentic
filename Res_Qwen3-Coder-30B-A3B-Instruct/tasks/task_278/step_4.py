import pandas as pd
import json
from collections import defaultdict, deque
import os

# Read all CSV files and infer schemas
csv_files = ['./company_mentions.csv', './crypto_prices.csv', './language_frequencies.csv', './email_detection_report.csv', './github_releases.csv', './top_python_repos.csv', './long_functions_report.csv', './python_files_line_counts.csv', './largest_files.csv', './config_report.csv', './file_size_histogram.csv', './image_dimensions.csv', './duplicated_headings_report.csv', './hacker_news_domains.csv', './repo_metadata.csv', './keyword_frequency.csv', './key_analysis.csv', './table_report.csv']

schemas = {}
for file in csv_files:
    try:
        df = pd.read_csv(file, nrows=100)  # Read first 100 rows for schema inference
        schemas[file] = {
            'columns': list(df.columns),
            'dtypes': df.dtypes.astype(str).to_dict()
        }
    except Exception as e:
        print(f"Error reading {file}: {e}")
        schemas[file] = {'columns': [], 'dtypes': {}}

print("Schemas inferred:")
for file, schema in schemas.items():
    print(f"{file}: {schema['columns']}")

# Identify potential foreign key relationships
relationships = []

# Define some common column names that might indicate relationships
foreign_key_indicators = ['id', 'ID', 'repo', 'name', 'url', 'file_path', 'path', 'domain', 'keyword']

for i, file1 in enumerate(csv_files):
    if not schemas[file1]['columns']:  # Skip empty schemas
        continue
    for j, file2 in enumerate(csv_files[i+1:], i+1):
        if not schemas[file2]['columns']:  # Skip empty schemas
            continue
            
        # Check for common columns that might indicate relationships
        common_columns = set(schemas[file1]['columns']) & set(schemas[file2]['columns'])
        
        # Filter for potential foreign keys
        potential_fk = [col for col in common_columns if col.lower() in foreign_key_indicators]
        
        if potential_fk:
            relationships.append({
                'file1': file1,
                'file2': file2,
                'common_columns': list(common_columns),
                'potential_foreign_keys': potential_fk
            })

print("\nPotential relationships identified:")
for rel in relationships:
    print(rel)