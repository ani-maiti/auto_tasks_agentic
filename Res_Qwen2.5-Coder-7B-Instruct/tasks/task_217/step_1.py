import requests
import csv

# List of popular Python repositories
repositories = [
    "https://api.github.com/repos/python/cpython",
    "https://api.github.com/repos/pandas-dev/pandas",
    "https://api.github.com/repos/numpy/numpy",
    "https://api.github.com/repos/scikit-learn/scikit-learn",
    "https://api.github.com/repos/requests/requests"
]

# Fetch data from GitHub API
data = []
for repo_url in repositories:
    response = requests.get(repo_url)
    if response.status_code == 200:
        repo_data = response.json()
        data.append({
            "name": repo_data["name"],
            "stars": repo_data["stargazers_count"],
            "forks": repo_data["forks_count"],
            "issues": repo_data["open_issues_count"]
        })

# Save data to CSV
with open("github_repos.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "stars", "forks", "issues"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("Data saved to github_repos.csv")