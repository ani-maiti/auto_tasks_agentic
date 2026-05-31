import requests

# List of popular Python repositories
repositories = [
    'numpy',
    'pandas',
    'scikit-learn',
    'tensorflow',
    'pytorch'
]

# Function to retrieve GitHub metadata for a repository
def get_repo_metadata(repo):
    url = f'https://api.github.com/repos/{repo}'
    response = requests.get(url)
    data = response.json()
    return {
        'stars': data['stargazers_count'],
        'forks': data['forks_count'],
        'issues': data['open_issues_count']
    }

# Create a list to store the metadata
metadata = []

# Retrieve metadata for each repository
for repo in repositories:
    metadata.append(get_repo_metadata(repo))

# Convert metadata to a DataFrame
import pandas as pd
df = pd.DataFrame(metadata)

# Save the DataFrame to a CSV file
df.to_csv('github_metadata.csv', index=False)

# Calculate average stars, forks, and issues
avg_stars = df['stars'].mean()
avg_forks = df['forks'].mean()
avg_issues = df['issues'].mean()

# Print the most starred repository
most_starred = df.sort_values('stars', ascending=False).iloc[0]
print(f'Most starred repository: {most_starred["stars"]} stars')