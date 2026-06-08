import json

# Load the data with rankings
with open('crypto_data_with_rankings.json', 'r') as f:
    data = json.load(f)

# Find asset with highest volatility
highest_volatility_asset = data[0]

# Generate report
report = {
    'total_assets': len(data),
    'highest_volatility_asset': {
        'name': highest_volatility_asset['name'],
        'symbol': highest_volatility_asset['symbol'],
        'volatility': highest_volatility_asset['volatility'],
        'market_cap_rank': highest_volatility_asset['market_cap_rank']
    },
    'top_5_by_volatility': [
        {
            'name': asset['name'],
            'symbol': asset['symbol'],
            'volatility': asset['volatility']
        }
        for asset in data[:5]
    ]
}

# Save report
with open('crypto_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print(f"Highest volatility asset: {highest_volatility_asset['name']} ({highest_volatility_asset['symbol']}) with {highest_volatility_asset['volatility']:.2f}% volatility")