import requests

url = "https://api.eoddata.com/api/v1/prices/latest?api_token=YOUR_API_TOKEN&symbols=XAGUSD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    silver_price = data[0]['Close']
    print(f"The current price of silver is ${silver_price}")
else:
    print("Failed to retrieve the price of silver from EODData")
```

Replace `YOUR_API_TOKEN` with your actual API token from EODData.