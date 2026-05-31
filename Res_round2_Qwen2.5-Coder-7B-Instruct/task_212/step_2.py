import requests

# Step 1: Find a public API for exchange rates
api_url = "https://api.exchangerate-api.com/v4/latest/USD"

# Step 2: Retrieve rates for USD against ten currencies
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    rates = data['rates']
    print(rates)
else:
    print("Failed to retrieve exchange rates.")
```

This code attempts to fetch the latest exchange rates for USD from the ExchangeRate-API. If successful, it extracts the rates into a dictionary and prints them. If not, it prints an error message.