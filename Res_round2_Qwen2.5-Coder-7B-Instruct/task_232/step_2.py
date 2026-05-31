import requests
import pandas as pd

# Step 2: Retrieve prices for the top fifty coins
response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false")
data = response.json()

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the dataset to CSV
df.to_csv('crypto_prices.csv', index=False)

# Print the first few rows of the DataFrame to confirm it contains the expected data
print(df.head())