import requests

# Fetch Ethereum price from CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
response = requests.get(url)
data = response.json()

# Extract and print the price
eth_price = data['ethereum']['usd']
print(f"Current Ethereum price: ${eth_price}")