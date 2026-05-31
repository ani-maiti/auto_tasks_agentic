import os
import glob
import pandas as pd

# Find all CSV files in the current directory
csv_files = glob.glob('*.csv')

print(f"Found {len(csv_files)} CSV files.")