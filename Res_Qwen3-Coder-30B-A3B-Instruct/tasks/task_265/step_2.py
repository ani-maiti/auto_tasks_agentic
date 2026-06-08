import pandas as pd
import re
from pathlib import Path

# Function to detect email-like patterns in a string
def contains_email(text):
    if pd.isna(text):
        return False
    # Simple regex for email detection
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.search(email_pattern, str(text)))

# Function to check if a column likely contains emails
def has_email_column(df):
    email_columns = []
    for col in df.columns:
        # Check if any value in the column looks like an email
        sample_values = df[col].sample(min(10, len(df)), random_state=1).dropna()
        if sample_values.apply(contains_email).any():
            email_columns.append(col)
    return email_columns

# Process all CSV files
all_reports = []

for csv_file in Path('.').glob('*.csv'):
    try:
        df = pd.read_csv(csv_file)
        email_cols = has_email_column(df)
        
        if email_cols:
            for col in email_cols:
                # Count how many rows have email-like content
                count = df[col].apply(contains_email).sum()
                all_reports.append({
                    'file': str(csv_file),
                    'column': col,
                    'email_count': int(count)
                })
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

# Create final report DataFrame
report_df = pd.DataFrame(all_reports)

# Save to CSV
report_df.to_csv('email_detection_report.csv', index=False)
print("Report saved to email_detection_report.csv")
print(report_df)