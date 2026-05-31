import requests
import pandas as pd

# Step 1: Retrieve exchange rates for fifty currencies relative to USD
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
exchange_rates = response.json()

# Extract the currency codes and rates
currency_codes = list(exchange_rates['rates'].keys())
rates = [exchange_rates['rates'][code] for code in currency_codes]

# Create a DataFrame to store the exchange rates
df = pd.DataFrame({'Currency': currency_codes, 'Rate': rates})

# Save the data to CSV
df.to_csv('exchange_rates.csv', index=False)

print("Exchange rates saved to exchange_rates.csv")