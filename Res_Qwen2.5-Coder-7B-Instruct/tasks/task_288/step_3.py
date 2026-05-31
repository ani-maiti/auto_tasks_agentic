import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("github_repos.csv")

# Group the data by language and calculate the total number of repositories per language
language_counts = df.groupby("language").size()

# Sort the languages by the number of repositories in descending order
sorted_languages = language_counts.sort_values(ascending=False)

# Get the most dominant language
most_dominant_language = sorted_languages.index[0]

# Print the most dominant language
print(f"The most dominant language is: {most_dominant_language}")