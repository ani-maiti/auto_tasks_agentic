import requests
import json
from collections import Counter

# GitHub API endpoint for searching repositories
url = "https://api.github.com/search/repositories"

# Parameters for the search
params = {
    'q': 'data-science',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 100
}

# Make the request
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit(1)

# Parse the JSON response
data = response.json()

# Extract repository metadata
repos = []
for item in data['items']:
    repo_info = {
        'name': item['name'],
        'full_name': item['full_name'],
        'description': item['description'],
        'language': item['language'],
        'stars': item['stargazers_count'],
        'forks': item['forks_count'],
        'url': item['html_url']
    }
    repos.append(repo_info)

# Save to JSON file
with open('data_science_repos.json', 'w') as f:
    json.dump(repos, f, indent=2)

print("Retrieved and saved metadata for 100 repositories")

# Classify by language and get statistics
languages = [repo['language'] for repo in repos if repo['language']]
language_counts = Counter(languages)

print("\nLanguage Statistics:")
for lang, count in language_counts.most_common():
    print(f"{lang}: {count}")