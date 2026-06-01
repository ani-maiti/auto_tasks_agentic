import requests

def fetch_exchange_rates(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch data from {url}: {e}")
        return None

providers = {
    "exchangerate-api": "https://v6.exchangerate-api.com/v6/5f2b0a0b1a0b1a0b1a0b1a0b/latest/USD",
    "openexchangerates": "https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID",  # Replace YOUR_APP_ID with a valid Open Exchange Rates app ID
    "fixer": "http://data.fixer.io/api/latest?access_key=YOUR_ACCESS_KEY&base=USD"  # Replace YOUR_ACCESS_KEY with a valid Fixer.io access key
}

rates = {}
for provider, url in providers.items():
    rates[provider] = fetch_exchange_rates(url)

print(rates)