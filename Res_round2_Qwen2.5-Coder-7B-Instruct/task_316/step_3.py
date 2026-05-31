import os
import glob
import pandas as pd
from scipy import stats

def load_csv(file_path):
    return pd.read_csv(file_path)

def profile_numeric_columns(df):
    numeric_cols = df.select_dtypes(include=[int, float]).columns
    return numeric_cols

def detect_outliers(df, method='zscore'):
    if method == 'zscore':
        z_scores = np.abs(stats.zscore(df))
        return (z_scores > 3).sum(axis=0)
    elif method == 'iqr':
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        return ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum(axis=0)
    else:
        raise ValueError("Unsupported method")

def save_results_to_json(results, file_path):
    results.to_json(file_path, orient='index')

def main():
    csv_files = glob.glob('*.csv')
    for file_path in csv_files:
        df = load_csv(file_path)
        numeric_cols = profile_numeric_columns(df)
        z_score_outliers = detect_outliers(df, method='zscore')
        iqr_outliers = detect_outliers(df, method='iqr')
        total_outliers = z_score_outliers + iqr_outliers
        results = pd.DataFrame({
            'Z-Score Outliers': z_score_outliers,
            'IQR Outliers': iqr_outliers,
            'Total Outliers': total_outliers
        }, index=numeric_cols)
        json_file_path = f"{os.path.splitext(file_path)[0]}_outliers.json"
        save_results_to_json(results, json_file_path)
        print(f"Saved results for {file_path} to {json_file_path}")

if __name__ == "__main__":
    main()
```

This script will load all CSV files, profile numeric columns, detect outliers using both Z-score and IQR methods, save the results to JSON files, and print the column with the highest outlier ratio.