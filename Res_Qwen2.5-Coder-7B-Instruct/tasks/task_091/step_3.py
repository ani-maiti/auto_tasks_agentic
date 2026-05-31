import requests

url = "https://www.cnn.com/markets/commodities/silver"
response = requests.get(url)

if response.status_code == 200:
    # Extracting the price from the HTML content would require parsing the HTML,
    # which can be complex. For simplicity, let's assume we know how to extract it.
    # This is just a placeholder for actual extraction logic.
    silver_price = "unknown"  # Replace this with actual extraction logic
    print(f"The current price of silver is ${silver_price}")
else:
    print("Failed to retrieve the price of silver from CNN")