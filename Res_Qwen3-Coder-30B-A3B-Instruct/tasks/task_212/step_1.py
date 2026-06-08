import requests
import json

# Using exchangerate-api.com as a free public exchange rate API
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Successfully retrieved exchange rate data")
    print(f"Base currency: {data['base']}")
    print(f"Date: {data['date']}")
    
    # Save raw data to file
    with open('exchange_rates_raw.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    # Get rates for 10 currencies
    currencies = ['EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'SEK', 'NZD', 'MXN']
    rates = {}
    
    for currency in currencies:
        if currency in data['rates']:
            rates[currency] = data['rates'][currency]
        else:
            print(f"Warning: {currency} not found in data")
    
    print("\nExchange rates for USD against 10 currencies:")
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")
    
    # Find strongest and weakest rates
    if rates:
        strongest = max(rates, key=rates.get)
        weakest = min(rates, key=rates.get)
        print(f"\nStrongest rate: {strongest} ({rates[strongest]})")
        print(f"Weakest rate: {weakest} ({rates[weakest]})")
    else:
        print("No valid rates found")
        
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")