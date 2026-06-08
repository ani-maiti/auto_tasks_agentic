import pandas as pd
import json
from datetime import datetime
import os
from dateutil import parser

# Store results
results = []

# Process each CSV file
for csv_file in [
    './company_mentions.csv',
    './crypto_prices.csv',
    './language_frequencies.csv',
    './email_detection_report.csv',
    './github_releases.csv',
    './weather_data_raw.csv',
    './top_python_repos.csv',
    './long_functions_report.csv',
    './python_files_line_counts.csv',
    './largest_files.csv',
    './config_report.csv',
    './file_size_histogram.csv',
    './image_dimensions.csv',
    './duplicated_headings_report.csv',
    './hacker_news_domains.csv',
    './repo_metadata.csv',
    './github_repos.csv',
    './keyword_frequency.csv',
    './weather_volatility.csv',
    './key_analysis.csv',
    './table_report.csv'
]:
    try:
        df = pd.read_csv(csv_file)
        
        # Find date columns
        date_columns = []
        for col in df.columns:
            # Check if column name contains 'date' or 'time'
            if 'date' in col.lower() or 'time' in col.lower():
                date_columns.append(col)
            else:
                # Check first few values for date-like patterns
                sample_values = df[col].dropna().head(10)
                date_count = 0
                for val in sample_values:
                    try:
                        if isinstance(val, str):
                            parser.parse(val)
                            date_count += 1
                        elif pd.notna(val) and isinstance(val, (pd.Timestamp, datetime)):
                            date_count += 1
                    except:
                        pass
                if date_count > len(sample_values) * 0.5:  # If more than half are dates
                    date_columns.append(col)
        
        if not date_columns:
            continue
            
        # Normalize dates and find ranges
        date_ranges = {}
        for col in date_columns:
            try:
                # Convert to datetime, handling various formats
                series = pd.to_datetime(df[col], errors='coerce')
                valid_dates = series.dropna()
                
                if len(valid_dates) > 0:
                    min_date = valid_dates.min()
                    max_date = valid_dates.max()
                    date_ranges[col] = {
                        'min': min_date.strftime('%Y-%m-%d'),
                        'max': max_date.strftime('%Y-%m-%d'),
                        'count': len(valid_dates)
                    }
            except Exception as e:
                print(f"Error processing {col} in {csv_file}: {e}")
        
        if date_ranges:
            # Calculate overall range for this dataset
            all_min_dates = [info['min'] for info in date_ranges.values()]
            all_max_dates = [info['max'] for info in date_ranges.values()]
            
            overall_min = min(all_min_dates) if all_min_dates else None
            overall_max = max(all_max_dates) if all_max_dates else None
            
            results.append({
                'file': csv_file,
                'date_columns': list(date_ranges.keys()),
                'date_ranges': date_ranges,
                'overall_range': {
                    'min': overall_min,
                    'max': overall_max
                }
            })
            
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

# Save to JSON
with open('dataset_analysis.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Analysis saved to dataset_analysis.json")