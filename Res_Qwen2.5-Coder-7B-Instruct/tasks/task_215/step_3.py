import pandas as pd

# Initialize an empty DataFrame to store the results
missing_values_df = pd.DataFrame(columns=['filename', 'column', 'percentage'])

# Loop through each CSV file and process it
for file in csv_files:
    df = pd.read_csv(file)
    for column in df.columns:
        missing_count = df[column].isna().sum()
        percentage = (missing_count / len(df)) * 100
        if percentage > 0:
            missing_values_df = missing_values_df.append({
                'filename': file,
                'column': column,
                'percentage': percentage
            }, ignore_index=True)

print(missing_values_df)