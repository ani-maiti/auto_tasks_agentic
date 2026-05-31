import os
import glob
import pandas as pd

# Load the first CSV file to check its structure
file_path = csv_files[0]
df = pd.read_csv(file_path)

# Identify columns containing dates
date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()

print(f"Date columns found: {date_columns}")