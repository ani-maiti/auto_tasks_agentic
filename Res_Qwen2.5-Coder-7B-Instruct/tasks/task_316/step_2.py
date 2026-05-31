import pandas as pd

# Function to profile numeric columns and detect outliers
def profile_and_detect_outliers(file):
    df = pd.read_csv(file)
    results = {}
    for col in df.select_dtypes(include=['number']).columns:
        # IQR method
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        iqr_outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        # Z-score method
        z_scores = (df[col] - df[col].mean()) / df[col].std()
        z_outliers = df[abs(z_scores) > 3]
        
        # Save results
        results[col] = {
            'IQR': {'outliers_count': len(iqr_outliers), 'outliers': list(iqr_outliers.index)},
            'Z-Score': {'outliers_count': len(z_outliers), 'outliers': list(z_outliers.index)}
        }
    return results

# Process each CSV file
outlier_results = {}
for csv_file in csv_files:
    print(f"Processing {csv_file}...")
    results = profile_and_detect_outliers(csv_file)
    outlier_results[csv_file] = results

# Save results to JSON
import json
with open('outlier_results.json', 'w') as f:
    json.dump(outlier_results, f, indent=4)

print("Outlier detection completed. Results saved to outlier_results.json")