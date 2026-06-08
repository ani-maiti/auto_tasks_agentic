import pandas as pd
import numpy as np
from pathlib import Path

# Function to find all CSV files
def find_csv_files():
    csv_files = list(Path('.').glob('*.csv'))
    return [str(f) for f in csv_files]

# Function to calculate correlations and generate report
def generate_correlation_report(csv_file):
    try:
        df = pd.read_csv(csv_file)
        
        # Select only numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return f"{csv_file}: Not enough numeric columns for correlation analysis"
        
        # Calculate correlation matrix
        corr_matrix = numeric_df.corr()
        
        # Find highly correlated pairs (threshold > 0.7 or < -0.7)
        highly_correlated = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                if abs(corr_value) > 0.7:
                    highly_correlated.append({
                        'File': csv_file,
                        'Column1': corr_matrix.columns[i],
                        'Column2': corr_matrix.columns[j],
                        'Correlation': corr_value
                    })
        
        return highly_correlated
        
    except Exception as e:
        return f"{csv_file}: Error processing file - {str(e)}"

# Main execution
csv_files = find_csv_files()
all_correlations = []

for csv_file in csv_files:
    result = generate_correlation_report(csv_file)
    if isinstance(result, list):
        all_correlations.extend(result)
    else:
        print(result)

# Generate markdown report
with open('correlation_report.md', 'w') as f:
    f.write("# Correlation Report\n\n")
    
    if not all_correlations:
        f.write("No highly correlated numeric columns found.\n")
    else:
        f.write("| File | Column 1 | Column 2 | Correlation |\n")
        f.write("|------|----------|----------|-------------|\n")
        for corr in all_correlations:
            f.write(f"| {corr['File']} | {corr['Column1']} | {corr['Column2']} | {corr['Correlation']:.3f} |\n")

print("Correlation report generated successfully.")