import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    ethereum_price = data['ethereum']['usd']
    print(f"The current Ethereum price in USD is: ${ethereum_price}")
else:
    print("Failed to retrieve Ethereum price.")