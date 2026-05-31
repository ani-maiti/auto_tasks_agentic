from requests import get

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
response = get(url)

if response.status_code == 200:
    data = response.json()
    price = data["ethereum"]["usd"]
    print(f"Current Ethereum price in USD: {price}")
else:
    print("Error fetching price")