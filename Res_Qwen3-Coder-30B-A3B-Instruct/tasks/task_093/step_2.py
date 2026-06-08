import json
import requests

# Fetch the data from GitHub API
url = "https://api.github.com/search/repositories?q=language:rust&sort=stars&order=desc&per_page=5"
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract and display the repository information
print("Top 5 most starred Rust repositories on GitHub:")
for i, repo in enumerate(data['items'], 1):
    print(f"{i}. {repo['full_name']} - {repo['stargazers_count']} stars")