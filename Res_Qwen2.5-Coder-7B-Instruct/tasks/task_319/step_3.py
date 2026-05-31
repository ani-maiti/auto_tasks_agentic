import requests
import pandas as pd

# Define the URLs for the exchange rate providers
urls = [
    "https://api.exchangerate-api.com/v4/latest/USD",
    "https://free.currencyconverterapi.com/api/v7/convert?q=USD_EUR&compact=ultra"
]

# Function to fetch exchange rates
def fetch_exchange_rates(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}")

# Fetch exchange rates from both providers
rates1 = fetch_exchange_rates(urls[0])
try:
    rates2 = fetch_exchange_rates(urls[1])
except Exception as e:
    print(f"Failed to fetch data from {urls[1]}: {e}")
    rates2 = None

# Extract the relevant exchange rates
if rates2 is not None:
    rate_usd_eur_1 = rates1['rates']['EUR']
    rate_usd_eur_2 = float(rates2['USD_EUR'])
else:
    rate_usd_eur_1 = rates1['rates']['EUR']
    rate_usd_eur_2 = None

# Create a DataFrame to store the exchange rates
df = pd.DataFrame({
    'Provider': ['ExchangeRate-API', 'CurrencyConverterAPI'],
    'USD_EUR': [rate_usd_eur_1, rate_usd_eur_2]
})

# Save the DataFrame to a CSV file
df.to_csv('exchange_rates.csv', index=False)

# Print the DataFrame
print(df)

# Check if we have valid rates to calculate discrepancy
if rate_usd_eur_2 is not None:
    # Calculate the discrepancy
    discrepancy = abs(rate_usd_eur_1 - rate_usd_eur_2)

    # Find the currency pair with the largest discrepancy
    largest_discrepancy_pair = ('USD/EUR', discrepancy)

    # Print the currency pair with the largest discrepancy
    print(largest_discrepancy_pair)
else:
    print("No valid exchange rate data available.")