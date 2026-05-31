import pandas as pd

# Initialize an empty list to store the results
results = []

# Loop through each CSV file and check for email-like columns
for file in csv_files:
    df = pd.read_csv(file)
    email_columns = []
    
    # Check each column for email patterns
    for col in df.columns:
        if df[col].astype(str).str.contains(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b').any():
            email_columns.append(col)
    
    if email_columns:
        results.append({'file': file, 'email_columns': email_columns})

# Save the results to a new CSV file
if results:
    result_df = pd.DataFrame(results)
    result_df.to_csv('email_report.csv', index=False)
    print("Email report saved to email_report.csv")
else:
    print("No email columns detected in any CSV files.")