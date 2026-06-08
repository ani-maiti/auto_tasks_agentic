import json
import requests
import statistics

# Load the saved data
with open('crypto_data.json', 'r') as f:
    data = json.load(f)

# Compute volatility for each asset (using price_change_percentage_24h)
for asset in data:
    if asset['price_change_percentage_24h'] is not None:
        asset['volatility'] = abs(asset['price_change_percentage_24h'])
    else:
        asset['volatility'] = 0

# Sort by market cap
data_sorted_by_market_cap = sorted(data, key=lambda x: x['market_cap'], reverse=True)

# Add market cap rank
for i, asset in enumerate(data_sorted_by_market_cap):
    asset['market_cap_rank'] = i + 1

# Sort by volatility
data_sorted_by_volatility = sorted(data, key=lambda x: x['volatility'], reverse=True)

# Add volatility rank
for i, asset in enumerate(data_sorted_by_volatility):
    asset['volatility_rank'] = i + 1

# Save updated data with rankings
with open('crypto_data_with_rankings.json', 'w') as f:
    json.dump(data_sorted_by_volatility, f)

print("Computed volatility and market cap rankings, saved updated dataset")