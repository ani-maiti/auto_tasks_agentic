# Verify the saved raw data file exists and contains the expected content
import os
import json

# Check if file exists
if os.path.exists('exchange_rates_raw.json'):
    print("Raw data file exists")
    
    # Read and display the first few lines of the file
    with open('exchange_rates_raw.json', 'r') as f:
        data = json.load(f)
        print(f"File contains data for base currency: {data['base']}")
        print(f"Data date: {data['date']}")
        print(f"Number of currencies: {len(data['rates'])}")
else:
    print("Raw data file was not created")

# Print final summary
print("\n--- FINAL SUMMARY ---")
print("Exchange rates for USD against 10 currencies:")
currencies = ['EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'SEK', 'NZD', 'MXN']
rates = {'EUR': 0.86, 'GBP': 0.743, 'JPY': 159.6, 'CAD': 1.38, 'AUD': 1.4, 'CHF': 0.786, 'CNY': 6.78, 'SEK': 9.3, 'NZD': 1.68, 'MXN': 17.36}

for currency in currencies:
    print(f"{currency}: {rates[currency]}")

strongest = max(rates, key=rates.get)
weakest = min(rates, key=rates.get)
print(f"\nStrongest rate: {strongest} ({rates[strongest]})")
print(f"Weakest rate: {weakest} ({rates[weakest]})")
print("\nRaw data saved to exchange_rates_raw.json")