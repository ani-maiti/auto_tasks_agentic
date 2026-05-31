import requests

# Set up the GitHub API endpoint
api_url = "https://api.github.com/repos/requests/requests/issues?state=open"

# Send a GET request to the API endpoint
response = requests.get(api_url)

# Check for successful response
if response.status_code == 200:
    # Get the number of issues from the response
    num_issues = len(response.json())
    
    # Print the number of issues
    print(f"Number of open issues: {num_issues}")
else:
    print(f"Error retrieving issues: {response.status_code}")