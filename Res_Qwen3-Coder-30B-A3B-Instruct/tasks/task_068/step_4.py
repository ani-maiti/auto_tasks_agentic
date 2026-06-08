import requests

# Download three random jokes and print them
for i in range(3):
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random", timeout=5)
        if response.status_code == 200:
            joke_data = response.json()
            print(f"Joke {i+1}: {joke_data['setup']} {joke_data['punchline']}")
        else:
            print(f"Failed to get joke {i+1}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error getting joke {i+1}: {e}")