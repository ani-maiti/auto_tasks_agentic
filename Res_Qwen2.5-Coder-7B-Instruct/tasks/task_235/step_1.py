import os

# Find all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
print(f"Found {len(csv_files)} CSV files.")