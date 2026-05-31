import requests

url = "https://api.exchangerate-api.com/v4/latest/GBP"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    gbp_usd_rate = data['rates']['USD']
    print(f"The current GBP/USD exchange rate is {gbp_usd_rate}")
else:
    print("Failed to retrieve the exchange rate")