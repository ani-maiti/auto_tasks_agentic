import pandas as pd
from datetime import datetime
import os

# Function to detect if a column contains dates
def has_date_format(series):
    # Try to parse the first few non-null values as dates
    sample = series.dropna().head(10)
    if len(sample) == 0:
        return False
    
    date_formats = [
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%m/%d/%Y',
        '%d/%m/%Y',
        '%Y-%m-%d %H:%M:%S',
        '%Y/%m/%d %H:%M:%S'
    ]
    
    for fmt in date_formats:
        try:
            pd.to_datetime(sample, format=fmt)
            return True
        except:
            continue
    
    # If standard formats don't work, try general parsing
    try:
        pd.to_datetime(sample)
        return True
    except:
        return False

# Process all CSV files
all_reports = []

for csv_file in ['./long_functions_report.csv', './python_files_line_counts.csv', './largest_files.csv', 
                 './config_report.csv', './file_size_histogram.csv', './repo_metadata.csv', './key_analysis.csv']:
    
    try:
        df = pd.read_csv(csv_file)
        
        # Find columns that might contain dates
        date_columns = []
        for col in df.columns:
            if has_date_format(df[col]):
                date_columns.append(col)
        
        # Compute date ranges for each date column
        date_ranges = {}
        for col in date_columns:
            try:
                # Convert to datetime if not already
                if not pd.api.types.is_datetime64_any_dtype(df[col]):
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                
                # Get min and max dates
                min_date = df[col].min()
                max_date = df[col].max()
                
                # Calculate range in days
                if pd.notna(min_date) and pd.notna(max_date):
                    range_days = (max_date - min_date).days
                    date_ranges[col] = {
                        'min': min_date,
                        'max': max_date,
                        'range_days': range_days
                    }
            except Exception as e:
                print(f"Error processing {col} in {csv_file}: {e}")
        
        # Store results
        all_reports.append({
            'filename': csv_file,
            'date_columns': date_columns,
            'date_ranges': date_ranges
        })
        
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")

# Save report to file
with open('date_range_report.txt', 'w') as f:
    for report in all_reports:
        f.write(f"File: {report['filename']}\n")
        f.write(f"Date columns: {report['date_columns']}\n")
        for col, info in report['date_ranges'].items():
            f.write(f"  Column '{col}': {info['min']} to {info['max']} ({info['range_days']} days)\n")
        f.write("\n")

# Find the widest date range
widest_range = None
widest_file = None
widest_column = None

for report in all_reports:
    for col, info in report['date_ranges'].items():
        if widest_range is None or info['range_days'] > widest_range:
            widest_range = info['range_days']
            widest_file = report['filename']
            widest_column = col

print(f"Widest date range: {widest_range} days")
print(f"File: {widest_file}")
print(f"Column: {widest_column}")