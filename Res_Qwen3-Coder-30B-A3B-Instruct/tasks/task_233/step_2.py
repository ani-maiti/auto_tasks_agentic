# Let's verify the contents of the saved JSON file
import json

with open('exchange_rates.json', 'r') as f:
    data = json.load(f)
    print(json.dumps(data, indent=2))