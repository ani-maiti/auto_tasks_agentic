import requests

response = requests.get("https://icanhazdadjoke.com/random")

if response.status_code == 200:
    joke = response.json()["joke"]
    print(joke)
else:
    print("Error retrieving joke")
```

This code block makes a GET request to the "https://icanhazdadjoke.com/random" API endpoint and checks the response status code. If the response is successful (status code 200), it extracts the joke from the JSON response and prints it. Otherwise, it prints an error message.