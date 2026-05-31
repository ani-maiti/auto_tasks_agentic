import requests
import csv

# Define the GitHub API endpoint for searching repositories
url = "https://api.github.com/search/repositories"

# Set the parameters for the API request
params = {
    "q": "topic:<selected_topic>",  # Replace <selected_topic> with the actual GitHub topic
    "sort": "stars",
    "order": "desc",
    "per_page": 100,
}

# Send the GET request to the GitHub API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    repositories = data["items"]
else:
    print("Failed to fetch repository data")
    exit(1)
```

This code snippet sends a GET request to the GitHub API to retrieve the top 100 repositories in a specified topic. It uses the `requests` library to handle the HTTP request. If the request is successful, it extracts the list of repositories from the JSON response. If the request fails, it prints an error message and exits.