import requests

url = "https://api.metals.live/api/v1/spot"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    gold_price = data["rates"]["XAU"]
    print(f"Current gold price: {gold_price}")
else:
    print(f"Error retrieving gold price: {response.status_code}")