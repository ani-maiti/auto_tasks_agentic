import requests
from bs4 import BeautifulSoup
import random

def fetch_joke():
    url = "https://www.jokes.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        joke_element = soup.find('div', {'class': 'text'})
        if joke_element:
            return joke_element.get_text(strip=True)
    return None

jokes = [fetch_joke() for _ in range(3)]
for joke in jokes:
    if joke:
        print(joke)
    else:
        print("Failed to fetch a joke.")
```

This code attempts to fetch three random jokes from the Jokes.com website and prints them. If it fails to fetch a joke, it will print a failure message.