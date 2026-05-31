import requests

# Step 1: Find a public cryptocurrency API
api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"

# Print the API URL to verify it's correct
print(api_url)