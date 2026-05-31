import requests

# Retrieve top 50 cryptocurrency prices
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
response = requests.get(url)

# Parse JSON response
data = response.json()

# Extract coin names and prices
coins = []
for coin in data:
    coins.append({
        "name": coin["name"],
        "symbol": coin["symbol"],
        "price": coin["current_price"],
        "market_cap": coin["market_cap"]
    })

# Calculate market rankings
for coin in coins:
    coin["rank"] = coins.index(coin) + 1

# Save dataset to CSV
with open("crypto_prices.csv", "w") as f:
    f.write("name,symbol,price,market_cap,rank\n")
    for coin in coins:
        f.write(f"{coin['name']},{coin['symbol']},{coin['price']},{coin['market_cap']},{coin['rank']}\n")

# Print top 10 coins
print("Top 10 Cryptocurrencies by Market Cap:")
for coin in coins[:10]:
    print(f"{coin['rank']}. {coin['name']} ({coin['symbol']}): ${coin['price']}")