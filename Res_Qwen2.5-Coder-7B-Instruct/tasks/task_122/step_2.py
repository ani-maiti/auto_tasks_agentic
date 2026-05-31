import requests

# Use the GitHub API to get the number of open issues in the requests repository
url = "https://api.github.com/repos/psf/requests/issues"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the number of open issues
    print(f"Number of open issues: {len(response.json())}")
else:
    # Print an error message if the request failed
    print(f"Failed to retrieve the number of open issues. Status code: {response.status_code}")