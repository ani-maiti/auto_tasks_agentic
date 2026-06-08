import requests
import csv
from datetime import datetime
import statistics

# Get the list of repositories from the GitHub organization
org_name = "microsoft"
url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100"

response = requests.get(url)
repos = response.json()

# Extract repository names
repo_names = [repo['name'] for repo in repos]

print(f"Found {len(repo_names)} repositories")
print("First 5 repositories:", repo_names[:5])