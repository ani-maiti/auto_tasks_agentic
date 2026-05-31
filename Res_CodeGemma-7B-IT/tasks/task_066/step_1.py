import requests

url = "https://api.exchangeratesapi.io/v1/latest?base=GBP&symbols=USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rate = data["rates"]["USD"]
    print(f"Current GBP/USD exchange rate: {rate}")
else:
    print("Error retrieving exchange rate.")