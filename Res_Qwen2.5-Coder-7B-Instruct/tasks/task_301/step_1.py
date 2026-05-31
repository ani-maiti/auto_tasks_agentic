import requests
import json

# Step 1: Retrieve metadata for the latest one hundred releases from a public GitHub organization
org_name = "octocat"
url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100"

response = requests.get(url)
if response.status_code == 200:
    repos = response.json()
    print("Retrieved repositories successfully.")
else:
    print(f"Failed to retrieve repositories. Status code: {response.status_code}")