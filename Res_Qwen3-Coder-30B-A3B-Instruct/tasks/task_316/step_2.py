import pandas as pd
import numpy as np
import json
from collections import defaultdict
import os

# Function to detect outliers using IQR method
def iqr_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series[(series < lower_bound) | (series > upper_bound)]

# Function to detect outliers using Z-score method
def zscore_outliers(series, threshold=3):
    z_scores = np.abs((series - series.mean()) / series.std())
    return series[z_scores > threshold]

# Function to detect outliers using modified Z-score method
def modified_zscore_outliers(series, threshold=3.5):
    median = series.median()
    mad = np.median(np.abs(series - median))
    modified_z_scores = 0.6745 * (series - median) / mad
    return series[np.abs(modified_z_scores) > threshold]

# Function to profile numeric columns and detect outliers
def profile_csv(file_path):
    df = pd.read_csv(file_path)
    results = {}
    
    # Get numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    for col in numeric_columns:
        series = df[col].dropna()
        if len(series) == 0:
            continue
            
        # Calculate basic statistics
        stats = {
            'count': len(series),
            'mean': float(series.mean()),
            'std': float(series.std()),
            'min': float(series.min()),
            'max': float(series.max()),
            'median': float(series.median())
        }
        
        # Detect outliers using different methods
        iqr_outlier_count = len(iqr_outliers(series))
        zscore_outlier_count = len(zscore_outliers(series))
        modified_zscore_outlier_count = len(modified_zscore_outliers(series))
        
        # Calculate outlier ratios
        iqr_ratio = iqr_outlier_count / len(series) if len(series) > 0 else 0
        zscore_ratio = zscore_outlier_count / len(series) if len(series) > 0 else 0
        modified_zscore_ratio = modified_zscore_outlier_count / len(series) if len(series) > 0 else 0
        
        results[col] = {
            'statistics': stats,
            'outliers': {
                'iqr': {
                    'count': iqr_outlier_count,
                    'ratio': iqr_ratio
                },
                'zscore': {
                    'count': zscore_outlier_count,
                    'ratio': zscore_ratio
                },
                'modified_zscore': {
                    'count': modified_zscore_outlier_count,
                    'ratio': modified_zscore_ratio
                }
            }
        }
    
    return results

# Find all CSV files
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Process each CSV file
all_results = {}

for file_path in csv_files:
    try:
        print(f"Processing {file_path}...")
        all_results[file_path] = profile_csv(file_path)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Save results to JSON
with open('outlier_detection_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)

print("Results saved to outlier_detection_results.json")
```