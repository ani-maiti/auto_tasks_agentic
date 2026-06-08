import json
import requests

# Fetch the top 5 Python repositories from GitHub API
url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=5"
response = requests.get(url)
data = response.json()

# Extract and display the repository information
repos = []
for item in data['items']:
    repos.append({
        'name': item['full_name'],
        'stars': item['stargazers_count']
    })

# Print the results
for i, repo in enumerate(repos, 1):
    print(f"{i}. {repo['name']} - {repo['stars']:,} stars")