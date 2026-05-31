import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URLs for the exchange rate providers
urls = [
    'https://www.exchangerate-api.com/v4/latest/USD',
    'https://api.exchangeratesapi.io/latest'
]

# Function to fetch exchange rates from a given URL
def fetch_exchange_rates(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}")

# Fetch exchange rates from both providers
try:
    exchange_rates_data = [fetch_exchange_rates(url) for url in urls]
except Exception as e:
    print(f"Error fetching exchange rates: {e}")
    # Fallback to a known good source if the first fails
    if "exchangerate-api.com" in str(e):
        urls[0] = 'https://api.exchangeratesapi.io/latest'
        exchange_rates_data = [fetch_exchange_rates(url) for url in urls]
    else:
        raise e

# Extract the base currency and rates
base_currencies = [data['base'] for data in exchange_rates_data]
rates = [data['rates'] for data in exchange_rates_data]

# Check if the base currencies are the same
if base_currencies[0] != base_currencies[1]:
    raise Exception("Base currencies differ between providers")

base_currency = base_currencies[0]

# Combine the rates into a single DataFrame
df = pd.DataFrame(rates).T
df.columns = ['rate_1', 'rate_2']
df['discrepancy'] = abs(df['rate_1'] - df['rate_2'])
df['currency_pair'] = df.index

# Save the dataset to CSV
df.to_csv('exchange_rates.csv')

# Find the currency pair with the largest discrepancy
largest_discrepancy_pair = df.loc[df['discrepancy'].idxmax(), 'currency_pair']

print(f"The currency pair with the largest discrepancy is: {largest_discrepancy_pair}")