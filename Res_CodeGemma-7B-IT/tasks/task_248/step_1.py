import os
import pandas as pd

# Get all CSV files in the current directory tree
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Create an empty dictionary to store column similarity matrices
column_similarity_matrices = {}

# Iterate over each pair of CSV files
for i in range(len(csv_files)):
    for j in range(i + 1, len(csv_files)):
        # Load the CSV files
        df1 = pd.read_csv(csv_files[i])
        df2 = pd.read_csv(csv_files[j])

        # Calculate the column similarity matrix
        column_similarity_matrix = df1.corrwith(df2)

        # Store the matrix in the dictionary
        column_similarity_matrices[(csv_files[i], csv_files[j])] = column_similarity_matrix

# Identify likely join relationships
join_relationships = []
for (file1, file2), matrix in column_similarity_matrices.items():
    # Find columns with high correlation
    correlated_columns = matrix[matrix > 0.8].dropna(axis=1).columns

    # Create a list of potential join relationships
    for column in correlated_columns:
        join_relationships.append((file1, file2, column))

# Generate a report
report = f"""
## Join Relationships Report

**CSV Files:**

* {', '.join(csv_files)}

**Potential Join Relationships:**

| File 1 | File 2 | Join Column |
|---|---|---|
{'\n'.join(['| '.join([f for f in join_relationship]) for join_relationship in join_relationships])}

**Note:** This report is based on column correlation. The actual join relationships may vary depending on the data in the files.
"""

# Save the report to JSON
with open('join_relationships.json', 'w') as f:
    f.write(report)