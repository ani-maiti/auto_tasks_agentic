from datetime import datetime

# Get current date and time
now = datetime.now()

# Format date and time
formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# Print timestamp
print(f"Current time: {formatted_time}")

# Import necessary libraries
import requests

# Define API endpoint for currency exchange rate
url = "https://openexchangerates.org/api/latest?symbols=EUR,USD&access_key=YOUR_API_KEY"

# Send GET request to API
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Extract exchange rate from response
    data = response.json()
    eur_usd_rate = data["rates"]["USD"]

    # Print current EUR/USD exchange rate
    print(f"Current EUR/USD exchange rate: {eur_usd_rate}")
else:
    # Handle API error
    print("Error retrieving exchange rate.")
```

**Note:**

- Replace `YOUR_API_KEY` with your actual Open Exchange Rates API key.
- This code fetches the current EUR/USD exchange rate from the Open Exchange Rates API.
- The output will include the current date and time, the exchange rate, and any error messages.