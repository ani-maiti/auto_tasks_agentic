import pandas as pd
import numpy as np

# Process each CSV file to find the worst column
worst_column = None
max_percentage = -1
worst_file = None

files = ['./long_functions_report.csv', './python_files_line_counts.csv', './largest_files.csv', './file_size_histogram.csv', './key_analysis.csv']

for csv_file in files:
    try:
        df = pd.read_csv(csv_file)
        total_rows = len(df)
        
        # Check each column for missing values
        for column in df.columns:
            missing_count = df[column].isnull().sum()
            # Handle case where total_rows might be 0
            if total_rows > 0:
                missing_percentage = (missing_count / total_rows) * 100
            else:
                missing_percentage = 0
                
            if missing_percentage > max_percentage:
                max_percentage = missing_percentage
                worst_column = column
                worst_file = csv_file
                
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

# Print the worst column
print(worst_column)

# Save quality report
with open('quality_report.txt', 'w') as f:
    f.write("CSV File Quality Report\n")
    f.write("======================\n\n")
    
    for csv_file in files:
        try:
            df = pd.read_csv(csv_file)
            total_rows = len(df)
            f.write(f"File: {csv_file}\n")
            
            for column in df.columns:
                missing_count = df[column].isnull().sum()
                # Handle case where total_rows might be 0
                if total_rows > 0:
                    missing_percentage = (missing_count / total_rows) * 100
                else:
                    missing_percentage = 0
                f.write(f"  {column}: {missing_count} missing ({missing_percentage:.2f}%)\n")
            
            f.write("\n")
        except Exception as e:
            f.write(f"Error processing {csv_file}: {e}\n\n")