import requests
import json

# Step 1: Retrieve current exchange rates for twenty currencies relative to USD
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    exchange_rates = data['rates']
else:
    print("Failed to fetch exchange rates")
```

This code retrieves the current exchange rates for various currencies relative to USD using the ExchangeRate-API. It checks if the request was successful and stores the exchange rates in a dictionary. If the request fails, it prints an error message.