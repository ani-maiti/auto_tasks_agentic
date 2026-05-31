import os

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
csv_files = [f for f in files if f.endswith('.csv')]

print("CSV Files:", csv_files)