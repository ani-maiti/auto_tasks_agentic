import requests

# Make a request to a random activity API
response = requests.get("https://www.boredapi.com/api/activity")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Print the activity suggestion
    print(data['activity'])
else:
    print(f"Failed to fetch activity. Status code: {response.status_code}")