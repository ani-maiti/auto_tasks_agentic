import requests
import json

# List of 20 currencies to check against USD
currencies = [
    "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN",
    "SGD", "HKD", "NOK", "TRY", "RUB", "INR", "BRL", "ZAR", "KRW", "ILS"
]

# Fetch exchange rates from a free API
try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    
    # Extract rates for our selected currencies
    rates = {}
    for currency in currencies:
        if currency in data['rates']:
            rates[currency] = data['rates'][currency]
        else:
            print(f"Warning: {currency} not found in exchange rate data")
    
    # Save to JSON file
    with open('exchange_rates.json', 'w') as f:
        json.dump(rates, f, indent=2)
    
    # Find the strongest currency (highest rate)
    if rates:
        strongest_currency = max(rates, key=rates.get)
        print(f"Strongest currency against USD: {strongest_currency} with rate {rates[strongest_currency]}")
    else:
        print("No valid exchange rates found")
        
except Exception as e:
    print(f"Error fetching data: {e}")