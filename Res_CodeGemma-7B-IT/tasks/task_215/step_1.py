import pandas as pd

# Find all CSV files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Create a list to store the missing value reports
reports = []

# Iterate over each CSV file
for file in files:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file)

    # Get the missing value counts by column
    missing_counts = df.isnull().sum()

    # Calculate the missing value percentages by column
    missing_percentages = missing_counts / len(df) * 100

    # Create a report for the current file
    report = {
        'file': file,
        'missing_counts': missing_counts,
        'missing_percentages': missing_percentages
    }

    # Add the report to the list
    reports.append(report)

# Find the worst column based on missing value percentage
worst_column = None
worst_percentage = 0

for report in reports:
    for column, percentage in report['missing_percentages'].items():
        if percentage > worst_percentage:
            worst_column = column
            worst_percentage = percentage

# Print the worst column
print('Worst column:', worst_column)