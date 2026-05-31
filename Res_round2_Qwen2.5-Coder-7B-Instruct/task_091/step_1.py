import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=silver&vs_currencies=usd"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    silver_price = data['silver']['usd']
    print(f"The current price of silver is ${silver_price}")
else:
    print("Failed to retrieve the price of silver.")