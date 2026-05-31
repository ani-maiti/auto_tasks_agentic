import requests
import csv
from collections import Counter

# Step 1: Retrieve metadata for the top fifty most starred Python repositories on GitHub
url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=50"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    repositories = data['items']
else:
    print("Failed to fetch repositories")
    exit(1)