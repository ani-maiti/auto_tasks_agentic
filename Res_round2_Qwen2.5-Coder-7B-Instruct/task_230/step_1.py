import requests
import json

# Step 1: Retrieve the latest one hundred GitHub repositories matching the topic 'machine-learning'
url = "https://api.github.com/search/repositories?q=topic:machine-learning&sort=created&order=desc&per_page=100"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    repositories = data['items']
else:
    print("Failed to fetch repositories")
    exit(1)