import requests
import json

# Get the contributors count from GitHub API
response = requests.get('https://api.github.com/repos/psf/requests/contributors')
contributors = response.json()

# Count the number of contributors
contributor_count = len(contributors)
print(contributor_count)