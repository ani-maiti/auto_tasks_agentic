import pandas as pd

# Step 3: Compute market rankings
df['market_rank'] = df['market_cap'].rank(ascending=False)

# Step 4: Save the updated dataset to CSV
df.to_csv('crypto_prices_with_rankings.csv', index=False)

# Print the top ten coins
top_ten_coins = df.head(10)
print(top_ten_coins[['id', 'symbol', 'current_price', 'market_cap', 'market_rank']])