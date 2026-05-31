import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    gold_price = data['bpi']['USD']['rate_float']
    print(f"The current price of gold is ${gold_price:.2f}")
else:
    print("Failed to retrieve the current price of gold.")