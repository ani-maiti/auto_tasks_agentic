import csv
from datetime import datetime

# Define a list of popular GitHub repositories
repositories = [
    "https://api.github.com/repos/python/cpython",
    "https://api.github.com/repos/nodejs/node",
    "https://api.github.com/repos/reactjs/react",
    # Add more repositories as needed
]

# Function to fetch the latest release date from a repository
def get_latest_release_date(repo_url):
    import requests
    response = requests.get(repo_url + "/releases/latest")
    if response.status_code == 200:
        data = response.json()
        return data['published_at']
    else:
        return None

# Fetch and store the latest release dates
release_dates = []
for repo in repositories:
    date = get_latest_release_date(repo)
    if date:
        release_dates.append((repo, date))

# Calculate the age of each release
current_date = datetime.now()
ages = [(repo, current_date - datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")) for repo, date in release_dates]

# Save the results to a CSV file
with open('release_age_report.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Repository', 'Release Age'])
    for repo, age in ages:
        writer.writerow([repo, age])

print("Release age report saved to release_age_report.csv")