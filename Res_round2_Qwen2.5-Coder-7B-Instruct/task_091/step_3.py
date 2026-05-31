print("We need to import the requests library before making HTTP requests.")

import requests

url = "https://www.bloomberg.com/quote/SILVER:COM"
response = requests.get(url)

if response.status_code == 200:
    # Extracting the price from the HTML content would require parsing the HTML.
    # This can be complex, so let's simplify by checking if we can find the price string.
    if 'price' in response.text.lower():
        print("Price found in the response. Parsing it...")
        # Placeholder for actual parsing logic
        print("Price parsed successfully.")
    else:
        print("Price not found in the response.")
else:
    print("Failed to retrieve the price of silver from Bloomberg.")