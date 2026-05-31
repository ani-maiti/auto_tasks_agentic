import os
import pandas as pd

# Get the current directory
cwd = os.getcwd()

# Find all CSV files in the directory tree
csv_files = [f for f in os.listdir(cwd) if f.endswith('.csv')]

# Initialize variables to store the largest file and its size
largest_file = None
largest_size = 0

# Iterate through the CSV files
for file in csv_files:
    # Get the file size
    file_size = os.path.getsize(file)

    # Update the largest file if necessary
    if file_size > largest_size:
        largest_size = file_size
        largest_file = file

# Print the largest file name
print(f"Largest CSV file: {largest_file}")

# Load the largest CSV file into a DataFrame
df = pd.read_csv(largest_file)

# Identify numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns

# Print the numeric columns
print(f"Numeric columns: {numeric_cols}")

# Compute summary statistics for each numeric column
summary_stats = df[numeric_cols].describe()

# Print the summary statistics
print(summary_stats)

# Find the column with the most variance
most_variable_col = summary_stats['var'].idxmax()

# Print the most variable column
print(f"Most variable column: {most_variable_col}")

# Save the results to a report
df.describe().to_csv("report.csv", index=True)