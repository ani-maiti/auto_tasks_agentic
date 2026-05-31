import requests
import json

# Step 1: Retrieve metadata for the latest one hundred releases from a public GitHub organization
organization = "octocat"  # Replace with the desired GitHub organization
url = f"https://api.github.com/orgs/{organization}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    repo_names = [repo['name'] for repo in repos]
    print(f"Retrieved {len(repo_names)} repositories.")
else:
    print("Failed to retrieve repositories.")
    exit(1)