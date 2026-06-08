import requests
import csv
from collections import defaultdict

# List of popular Python repositories
repos = [
    "python/cpython",
    "django/django",
    "pallets/flask",
    "requests/requests",
    "numpy/numpy"
]

# Function to get repository metadata
def get_repo_metadata(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['full_name'],
            'stars': data['stargazers_count'],
            'forks': data['forks_count'],
            'open_issues': data['open_issues_count']
        }
    else:
        print(f"Error fetching {owner}/{repo}: {response.status_code}")
        return None

# Fetch metadata for all repositories
metadata_list = []
for repo in repos:
    owner, name = repo.split("/")
    meta = get_repo_metadata(owner, name)
    if meta:
        metadata_list.append(meta)

# Save to CSV
with open('repo_metadata.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'stars', 'forks', 'open_issues']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for meta in metadata_list:
        writer.writerow(meta)

print("Repository metadata saved to repo_metadata.csv")