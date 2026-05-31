import requests
import json
from datetime import datetime, timedelta

# Define the API endpoint
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Function to fetch exchange rates
def fetch_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch exchange rates")

# Main loop to fetch rates every minute for 10 minutes
for i in range(10):
    try:
        rates_data = fetch_exchange_rates()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Timestamp: {timestamp}")
        print(json.dumps(rates_data, indent=4))
        # Save the data to a file
        with open(f"exchange_rates_{i}.json", "w") as f:
            json.dump(rates_data, f)
        print(f"Data saved to exchange_rates_{i}.json")
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
    time.sleep(60)
```

This script fetches exchange rates from the specified API endpoint every minute for 10 minutes, saves the data to a JSON file, and prints the timestamp along with the fetched data.