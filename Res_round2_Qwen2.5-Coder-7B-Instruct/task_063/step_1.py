import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    bitcoin_price_usd = data['bpi']['USD']['rate_float']
    print(f"Current Bitcoin price in USD: {bitcoin_price_usd}")
else:
    print("Failed to fetch Bitcoin price")