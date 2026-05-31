import pandas as pd

# Get a list of all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Create an empty list to store the correlation reports
reports = []

# Iterate over each CSV file
for csv_file in csv_files:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Identify columns with highly correlated numeric values
    correlated_cols = df.corr().unstack().sort_values(ascending=False)

    # Create a correlation report for the current file
    report = f"## Correlation Report for {csv_file}\n\n"
    report += f"Columns with highly correlated numeric values:\n"
    report += f"{correlated_cols[correlated_cols > 0.8]}\n\n"

    # Add the report to the list of reports
    reports.append(report)

# Save the correlation reports to a Markdown file
with open('correlation_reports.md', 'w') as f:
    f.write('\n'.join(reports))

# Print a success message
print("Correlation reports generated successfully.")