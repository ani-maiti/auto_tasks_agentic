import requests

# Get the repository information
response = requests.get("https://api.github.com/repos/requests/requests")

# Extract the number of forks
forks = response.json()["forks"]

# Print the number of forks
print(forks)