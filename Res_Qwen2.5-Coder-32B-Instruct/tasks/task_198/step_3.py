import pandas as pd

file_with_max_rows = './python_files_line_counts.csv'
df = pd.read_csv(file_with_max_rows)

numeric_cols = df.select_dtypes(include=['number']).columns
print(f"Numeric columns: {list(numeric_cols)}")