import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    bitcoin_price_usd = data['bpi']['USD']['rate_float']
    print(f"Current Bitcoin price in USD: ${bitcoin_price_usd:.2f}")
else:
    print("Failed to retrieve Bitcoin price.")
```

This code attempts to fetch the current Bitcoin price in USD from the Coindesk API and prints it if successful. If the request fails, it prints an error message.