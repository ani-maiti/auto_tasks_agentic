import requests
import csv
from datetime import datetime

# List of fifty popular GitHub repositories
repositories = [
    "https://api.github.com/repos/torvalds/linux",
    "https://api.github.com/repos/facebook/react",
    "https://api.github.com/repos/microsoft/vscode",
    "https://api.github.com/repos/nodejs/node",
    "https://api.github.com/repos/angular/angular",
    # Add more repositories as needed
]

# Function to get the latest release date for a repository
def get_latest_release_date(repo_url):
    response = requests.get(repo_url + "/releases/latest")
    if response.status_code == 200:
        data = response.json()
        return data['published_at']
    else:
        return None

# Fetch and store the latest release dates
release_dates = []
for repo in repositories:
    latest_release_date = get_latest_release_date(repo)
    if latest_release_date:
        release_dates.append((repo.split('/')[-1], latest_release_date))

# Calculate release age
current_date = datetime.now()
release_age_data = []
for repo, date_str in release_dates:
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    age = current_date - date_obj
    release_age_data.append((repo, date_str, age.days))

# Save to CSV
with open('release_age_report.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Repository', 'Latest Release Date', 'Release Age (days)'])
    writer.writerows(release_age_data)

print("Release age report saved to release_age_report.csv")