import requests

# Download three random jokes and print them
jokes = []
for i in range(3):
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random", timeout=5)
        if response.status_code == 200:
            joke_data = response.json()
            # Format the joke nicely
            joke = f"{joke_data['setup']} {joke_data['punchline']}"
            jokes.append(joke)
        else:
            print(f"Failed to get joke {i+1}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error getting joke {i+1}: {e}")

# Print all jokes
for i, joke in enumerate(jokes, 1):
    print(f"Joke {i}: {joke}")