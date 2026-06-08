import requests
import json
import statistics

# Retrieve cryptocurrency market data for top 100 assets
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False
}

response = requests.get(url, params=params)
data = response.json()

# Save raw data to JSON file
with open('crypto_data.json', 'w') as f:
    json.dump(data, f)

print("Retrieved and saved cryptocurrency data for top 100 assets")