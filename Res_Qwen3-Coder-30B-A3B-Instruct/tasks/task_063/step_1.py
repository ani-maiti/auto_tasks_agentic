import requests

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    print(f"Current Bitcoin price in USD: {price}")
except Exception as e:
    print(f"Error fetching Bitcoin price: {e}")