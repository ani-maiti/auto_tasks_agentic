import requests

url = "https://api.exchangerate-api.com/v4/latest/EUR"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    eur_usd_rate = data['rates']['USD']
    print(f"Current EUR/USD exchange rate: {eur_usd_rate}")
else:
    print("Failed to retrieve exchange rate")