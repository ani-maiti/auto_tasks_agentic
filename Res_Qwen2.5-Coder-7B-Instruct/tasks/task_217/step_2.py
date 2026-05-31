import pandas as pd

# Load data from CSV
df = pd.read_csv("github_repos.csv")

# Compute averages
averages = df.mean()

# Print the most starred repository
most_starred_repo = df.loc[df['stars'].idxmax()]
print(f"Most starred repository: {most_starred_repo['name']} with {most_starred_repo['stars']} stars")