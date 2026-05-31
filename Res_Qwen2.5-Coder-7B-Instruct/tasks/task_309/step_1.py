import requests
import json

# Step 1: Retrieve cryptocurrency market data for the top one hundred assets
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")