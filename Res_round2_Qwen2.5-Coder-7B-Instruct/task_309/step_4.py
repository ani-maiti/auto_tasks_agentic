import pandas as pd

# Assuming 'data' is already defined from the previous step
# Convert the fetched data into a DataFrame
df = pd.DataFrame(data)

# Compute volatility and market cap rankings
df['volatility'] = df['price_change_percentage_24h'].abs()  # Simplified volatility calculation
df['market_cap_rank'] = df['market_cap'].rank(ascending=False)

# Save the dataset to JSON
df.to_json('crypto_data.json', orient='records')

print("Dataset saved to crypto_data.json")