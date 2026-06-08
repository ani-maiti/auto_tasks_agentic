import requests

# Make a request to a random joke API
response = requests.get("https://official-joke-api.appspot.com/jokes/random")

# Check if the request was successful
if response.status_code == 200:
    joke_data = response.json()
    print(f"{joke_data['setup']} {joke_data['punchline']}")
else:
    print("Failed to fetch joke")