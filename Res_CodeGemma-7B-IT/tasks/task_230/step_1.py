# Import necessary libraries
import requests
import json
from collections import defaultdict

# Define the API endpoint and parameters
url = "https://api.github.com/search/repositories"
params = {"q": "machine-learning", "sort": "stars", "order": "desc", "per_page": 100}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code != 200:
    print("Error:", response.status_code)
    exit()

# Parse the JSON response
data = response.json()

# Extract repository information
repositories = data["items"]

# Calculate average stars and forks
total_stars = 0
total_forks = 0
for repo in repositories:
    total_stars += repo["stargazers_count"]
    total_forks += repo["forks_count"]

average_stars = total_stars / len(repositories)
average_forks = total_forks / len(repositories)

# Create a dictionary of results
results = {
    "average_stars": average_stars,
    "average_forks": average_forks,
    "most_starred_repository": max(repositories, key=lambda repo: repo["stargazers_count"])["name"]
}

# Save results to a JSON file
with open("results.json", "w") as f:
    json.dump(results, f)

# Print the most starred repository
print("Most Starred Repository:", results["most_starred_repository"])