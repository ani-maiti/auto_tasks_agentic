import requests

# Use GitHub API to get the number of contributors
response = requests.get('https://api.github.com/repos/psf/requests/contributors')

# Check if the request was successful
if response.status_code == 200:
    # Print the number of contributors
    print("Number of contributors:", len(response.json()))
else:
    # Print an error message if the request failed
    print("Failed to retrieve contributors:", response.text)