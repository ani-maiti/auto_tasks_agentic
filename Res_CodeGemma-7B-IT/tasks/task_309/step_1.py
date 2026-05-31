import pandas as pd
import requests

# Retrieve cryptocurrency market data for the top 100 assets
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
response = requests.get(url)

# Create a DataFrame from the JSON data
df = pd.DataFrame(response.json())

# Compute volatility and market cap rankings
df['volatility'] = (df['high_24h'] - df['low_24h']) / df['current_price']
df['market_cap_rank'] = df['market_cap'].rank(ascending=False)

# Save the dataset to JSON
df.to_json('crypto_data.json', orient='records')

# Generate a report
report = f"Top 100 Cryptocurrencies\n\n"
report += f"Asset\tVolatility\tMarket Cap Rank\n"
for _, row in df.iterrows():
    report += f"{row['name']}\t{row['volatility']:.2%}\t{row['market_cap_rank']}\n"

# Print the asset with the highest volatility
highest_volatility_asset = df[df['volatility'] == df['volatility'].max()]
print(f"Asset with the highest volatility:\n{highest_volatility_asset[['name', 'volatility']]}")