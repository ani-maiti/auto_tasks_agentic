import requests
import pandas as pd

# Step 1: Retrieve exchange rates for fifty currencies relative to USD
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
exchange_rates = response.json()["rates"]

# Save the exchange rates to a CSV file
df = pd.DataFrame(list(exchange_rates.items()), columns=['Currency', 'Rate'])
df.to_csv('exchange_rates.csv', index=False)

print("Exchange rates retrieved and saved to exchange_rates.csv")