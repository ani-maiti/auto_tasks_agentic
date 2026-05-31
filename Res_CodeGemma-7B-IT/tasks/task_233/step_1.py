# Import necessary libraries
import requests
import json

# Define the currencies to retrieve rates for
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD', 'ZAR', 'KRW', 'RUB', 'TRY', 'INR', 'IDR', 'MXN', 'THB', 'AED', 'SAR']

# Function to retrieve currency rates from API
def get_exchange_rates():
  url = "https://api.exchangeratesapi.io/v1/latest?base=USD&symbols=" + ",".join(currencies)
  response = requests.get(url)
  return response.json()

# Get currency rates
rates = get_exchange_rates()

# Compute currency strength rankings
currency_strengths = []
for currency, rate in rates['rates'].items():
  currency_strengths.append((currency, rate))

currency_strengths.sort(key=lambda x: x[1], reverse=True)

# Save results to JSON
with open('currency_strengths.json', 'w') as f:
  json.dump(currency_strengths, f)

# Print strongest currency
strongest_currency = currency_strengths[0][0]
print(f"Strongest currency: {strongest_currency}")