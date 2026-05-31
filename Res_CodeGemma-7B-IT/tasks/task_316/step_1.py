import os
import csv
import pandas as pd
import numpy as np
from scipy.stats import iqr, mad, zscore

# Get the list of CSV files in the current directory
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# Create an empty list to store the outlier ratios for each column
outlier_ratios = []

# Iterate over each CSV file
for csv_file in csv_files:
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns

    # Calculate outlier ratios for each numeric column
    for col in numeric_cols:
        # Calculate quartiles and interquartile range (IQR)
        q25, q75 = df[col].quantile([0.25, 0.75])
        iqr_value = q75 - q25

        # Calculate mean absolute deviation (MAD)
        mad_value = mad(df[col])

        # Calculate z-scores and identify outliers
        z_scores = zscore(df[col])
        outliers = df[np.abs(z_scores) > 3]

        # Calculate the outlier ratio
        outlier_ratio = len(outliers) / len(df[col])

        # Store the outlier ratio for this column
        outlier_ratios.append({
            'file': csv_file,
            'column': col,
            'outlier_ratio': outlier_ratio
        })

# Create a DataFrame from the outlier ratios
outlier_df = pd.DataFrame(outlier_ratios)

# Save the outlier ratios to a JSON file
outlier_df.to_json('outlier_ratios.json', orient='records')

# Print the column with the highest outlier ratio
print(outlier_df.sort_values('outlier_ratio', ascending=False).head(1)['column'])