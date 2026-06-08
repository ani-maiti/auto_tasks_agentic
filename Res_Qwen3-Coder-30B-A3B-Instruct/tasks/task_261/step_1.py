import requests
import time
import json
from collections import defaultdict
import statistics

# Initialize data storage
exchange_rates_data = []
volatility_metrics = defaultdict(list)

# Function to fetch exchange rates
def fetch_exchange_rates():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Fetch data for 10 minutes (every minute)
print("Starting exchange rate monitoring...")
for i in range(10):
    print(f"Fetching data for minute {i+1}...")
    data = fetch_exchange_rates()
    
    if data:
        # Store the data
        exchange_rates_data.append({
            "timestamp": time.time(),
            "rates": data["rates"]
        })
        
        # Calculate volatility for each currency (using standard deviation of last 5 readings)
        if len(exchange_rates_data) >= 2:
            latest_rates = data["rates"]
            previous_rates = exchange_rates_data[-2]["rates"]
            
            for currency, rate in latest_rates.items():
                if currency in previous_rates:
                    # Calculate percentage change
                    change = abs((rate - previous_rates[currency]) / previous_rates[currency])
                    volatility_metrics[currency].append(change)
    
    time.sleep(60)  # Wait for 1 minute

# Save data to file
with open('exchange_rates.json', 'w') as f:
    json.dump(exchange_rates_data, f)

print("Data saved to exchange_rates.json")

# Calculate final volatility metrics
final_volatility = {}
for currency, changes in volatility_metrics.items():
    if len(changes) >= 2:
        # Use standard deviation of percentage changes
        final_volatility[currency] = statistics.stdev(changes)

# Find most volatile currency
if final_volatility:
    most_volatile_currency = max(final_volatility, key=final_volatility.get)
    print(f"Most volatile currency: {most_volatile_currency} with volatility: {final_volatility[most_volatile_currency]:.6f}")
else:
    print("Not enough data to calculate volatility")