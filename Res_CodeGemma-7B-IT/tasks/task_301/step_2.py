# Fix the API endpoint to use the correct organization name
RELEASES_URL = f"https://api.github.com/orgs/{ORG_NAME}/releases"

# Execute the code block
```python
import requests
from datetime import datetime, timedelta

# GitHub organization name
ORG_NAME = "pytorch"

# Number of releases to retrieve
NUM_RELEASES = 100

# API endpoint for releases
RELEASES_URL = f"https://api.github.com/orgs/{ORG_NAME}/releases"

# Retrieve release data
response = requests.get(RELEASES_URL)

# Check for errors
if response.status_code != 200:
    print(f"Error retrieving releases: {response.status_code}")
    exit()

# Extract release information
releases = response.json()

# Create a list of release objects
release_objects = []
for release in releases:
    release_objects.append({
        "name": release["name"],
        "published_at": datetime.strptime(release["published_at"], "%Y-%m-%dT%H:%M:%SZ"),
        "tag_name": release["tag_name"],
        "repository": release["repository"]["name"],
    })

# Calculate release frequency statistics
release_dates = [release["published_at"] for release in release_objects]
date_range = max(release_dates) - min(release_dates)
days_in_range = (date_range.days + 1)
release_frequency = len(release_dates) / days_in_range

# Save dataset to CSV
with open("releases.csv", "w") as f:
    f.write("name,published_at,tag_name,repository\n")
    for release in release_objects:
        f.write(f"{release['name']},{release['published_at']},{release['tag_name']},{release['repository']}\n")

# Generate report
print(f"Number of releases: {len(release_objects)}")
print(f"Release frequency: {release_frequency:.2f} releases per day")

# Find repository with highest release frequency
repository_counts = {}
for release in release_objects:
    repository_counts.setdefault(release["repository"], 0)
    repository_counts[release["repository"]] += 1
highest_frequency_repo = max(repository_counts, key=repository_counts.get)
print(f"Repository with highest release frequency: {highest_frequency_repo}")