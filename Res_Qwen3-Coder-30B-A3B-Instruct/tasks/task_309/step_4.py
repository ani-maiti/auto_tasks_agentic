import json

# Load the final report
with open('crypto_report.json', 'r') as f:
    report = json.load(f)

# Print the asset with highest volatility
highest = report['highest_volatility_asset']
print(f"Asset with highest volatility: {highest['name']} ({highest['symbol']})")
print(f"Volatility: {highest['volatility']:.2f}%")
print(f"Market cap rank: {highest['market_cap_rank']}")