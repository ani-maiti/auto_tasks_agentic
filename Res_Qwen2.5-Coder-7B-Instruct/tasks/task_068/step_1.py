import requests
import json

def get_random_joke():
    response = requests.get('https://official-joke-api.appspot.com/jokes/random')
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['setup'], joke_data['punchline']
    else:
        return None, None

for _ in range(3):
    setup, punchline = get_random_joke()
    if setup and punchline:
        print(f"Joke:\n{setup}\n{punchline}\n")
    else:
        print("Failed to retrieve a joke.")
```

This script attempts to fetch three random jokes from an API and prints them. If it fails to retrieve a joke, it will print a failure message.