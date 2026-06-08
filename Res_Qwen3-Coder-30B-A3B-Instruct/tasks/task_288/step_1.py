import requests
import csv
from collections import Counter
import pandas as pd

# Define the GitHub API endpoint for searching repositories
def get_repositories(topic, count=100):
    url = f"https://api.github.com/search/repositories"
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {
        "q": f"topic:{topic}",
        "sort": "stars",
        "order": "desc",
        "per_page": count
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()["items"]
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

# Get top 100 repositories for the 'python' topic
repos = get_repositories("python", 100)

# Print number of repos retrieved
print(f"Retrieved {len(repos)} repositories")

# Extract required information
repo_data = []
for repo in repos:
    repo_info = {
        "name": repo["full_name"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "issues": repo["open_issues_count"],
        "language": repo["language"]
    }
    repo_data.append(repo_info)

# Save to CSV
with open('github_repos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["name", "stars", "forks", "issues", "language"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(repo_data)

print("Data saved to github_repos.csv")