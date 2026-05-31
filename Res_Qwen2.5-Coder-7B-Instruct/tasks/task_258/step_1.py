import requests
import json

# Fetch the top 100 GitHub repositories tagged with 'data-science'
url = "https://api.github.com/search/repositories?q=topic:data-science&sort=stars&order=desc&per_page=100"
response = requests.get(url)

if response.status_code == 200:
    repositories = response.json()['items']
    print("Fetched", len(repositories), "repositories.")
else:
    print("Failed to fetch repositories:", response.status_code)
    exit(1)