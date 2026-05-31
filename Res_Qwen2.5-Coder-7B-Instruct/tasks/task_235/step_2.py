import pandas as pd

# Function to detect potential primary key columns
def detect_primary_key_columns(file_path):
    df = pd.read_csv(file_path)
    # Check for unique values in each column
    unique_counts = df.nunique()
    # Columns with more than 50% unique values might be good candidates
    potential_pk_columns = unique_counts[unique_counts > len(df) * 0.5].index.tolist()
    return potential_pk_columns

# Apply the function to each CSV file and store results
results = {}
for csv_file in csv_files:
    pk_columns = detect_primary_key_columns(csv_file)
    results[csv_file] = pk_columns

print("Potential primary key columns detected:")
for file, columns in results.items():
    print(f"{file}: {columns}")