import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('python_files_line_counts.csv')

# Sort the DataFrame by line count in descending order
df_sorted = df.sort_values(by='Line Count', ascending=False)

# Save the sorted DataFrame back to the CSV file
df_sorted.to_csv('python_files_line_counts_sorted.csv', index=False)

print("Sorted CSV file generated successfully.")