import pandas as pd

# Read the CSV file and analyze the data
df = pd.read_csv('github_repos.csv')

# Display basic info about the dataset
print("Dataset Info:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Calculate rankings based on stars
df_sorted = df.sort_values('stars', ascending=False)
print("\nTop 5 repositories by stars:")
print(df_sorted[['name', 'stars']].head())

# Compute language distribution
language_counts = df['language'].value_counts()
print("\nLanguage distribution:")
print(language_counts)

# Find the most dominant language
most_dominant_language = language_counts.index[0]
print(f"\nMost dominant language: {most_dominant_language}")