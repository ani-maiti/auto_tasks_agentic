import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('release_age_report.csv')

# Convert the Release Age column to a more readable format
df['Release Age'] = df['Release Age'].apply(lambda x: str(x).split()[0] + ' days ago')

# Display the first few rows of the DataFrame
print(df.head())