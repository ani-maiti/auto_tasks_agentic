# Print the strongest currency as requested
import json

with open('exchange_rates.json', 'r') as f:
    data = json.load(f)

strongest_currency = max(data, key=data.get)
print(f"The strongest currency against USD is {strongest_currency} with a rate of {data[strongest_currency]}")