import requests

# Set the base URL for the API
base_url = "https://api.exchangeratesapi.io/v1/"

# Set the API key
api_key = "YOUR_API_KEY"

# Set the currencies to retrieve rates for
currencies = ["EUR", "GBP", "JPY", "CAD", "AUD", "NZD", "CHF", "SEK", "DKK", "NOK"]

# Create a dictionary to store the rates
rates = {}

# Loop through the currencies and retrieve the rates
for currency in currencies:
    url = f"{base_url}latest?base=USD&symbols={currency}"
    response = requests.get(url, headers={"apikey": api_key})
    data = response.json()
    rates[currency] = data["rates"][currency]

# Print the raw data
print(rates)

# Find the strongest and weakest rates
strongest_rate = max(rates.values())
weakest_rate = min(rates.values())

# Print the summary
print("Strongest rate:", strongest_rate)
print("Weakest rate:", weakest_rate)