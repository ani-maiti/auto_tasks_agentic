import requests

# Step 1: Find a public API for exchange rates
api_url = "https://api.exchangerate-api.com/v4/latest/USD"

response = requests.get(api_url)

if response.status_code == 200:
    print("API found successfully.")
else:
    print("Failed to find an API. Exiting.")
    exit(1)
```

This code attempts to find a public API for exchange rates by making a request to a known service. If successful, it prints a success message; otherwise, it exits with an error message.