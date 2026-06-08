import pandas as pd

# Read the CSV file and analyze the data
df = pd.read_csv('github_repos.csv')

# Generate a comprehensive report
print("=" * 50)
print("GITHUB REPOSITORIES REPORT")
print("=" * 50)
print(f"Total repositories analyzed: {len(df)}")
print(f"Repositories with language data: {len(df[df['language'].notnull()])}")
print(f"Repositories without language data: {len(df[df['language'].isnull()])}")

print("\nTOP 10 REPOSITORIES BY STARS:")
top_10 = df.sort_values('stars', ascending=False).head(10)[['name', 'stars', 'forks', 'issues', 'language']]
for index, row in top_10.iterrows():
    print(f"{index+1}. {row['name']} - Stars: {row['stars']}, Language: {row['language']}")

print("\nLANGUAGE DISTRIBUTION:")
language_counts = df['language'].value_counts()
for lang, count in language_counts.items():
    percentage = (count / len(df)) * 100
    print(f"{lang}: {count} repositories ({percentage:.1f}%)")

print(f"\nMOST DOMINANT LANGUAGE: {language_counts.index[0]}")
print("=" * 50)