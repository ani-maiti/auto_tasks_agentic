import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    gold_price = data['bpi']['USD']['rate_float']
    print(f"Current price of gold: ${gold_price}")
else:
    print("Failed to retrieve gold price")