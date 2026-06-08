import requests

# Download three random jokes and print them
jokes = []
for i in range(3):
    response = requests.get("https://official-joke-api.appspot.com/jokes/random", timeout=5)
    if response.status_code == 200:
        joke_data = response.json()
        joke = f"{joke_data['setup']} {joke_data['punchline']}"
        jokes.append(joke)

# Print the jokes
for i, joke in enumerate(jokes, 1):
    print(f"Joke {i}: {joke}")