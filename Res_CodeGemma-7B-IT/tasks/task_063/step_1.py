import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    usd_price = data["bpi"]["USD"]["rate_float"]
    print(f"Current Bitcoin price in USD: {usd_price}")
else:
    print("Error fetching data.")