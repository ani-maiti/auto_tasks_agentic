import requests

try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/GBP")
    data = response.json()
    usd_rate = data["rates"]["USD"]
    print(f"Current GBP/USD exchange rate: {usd_rate}")
except Exception as e:
    print(f"Error retrieving exchange rate: {e}")