import requests

# Define the API endpoint for random jokes
joke_api_url = "https://api.chucknorris.io/jokes/random"

# Get the first joke
response = requests.get(joke_api_url)

# Print the first joke
print(response.json()['value'])

# Get the second joke
response = requests.get(joke_api_url)

# Print the second joke
print(response.json()['value'])

# Get the third joke
response = requests.get(joke_api_url)

# Print the third joke
print(response.json()['value'])