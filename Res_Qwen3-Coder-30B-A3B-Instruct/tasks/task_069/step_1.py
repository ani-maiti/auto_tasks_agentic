import requests

try:
    response = requests.get("https://api.quotable.io/random")
    response.raise_for_status()
    quote_data = response.json()
    print(f"Quote: {quote_data['content']}")
    print(f"Author: {quote_data['author']}")
except Exception as e:
    print(f"Error: {e}")