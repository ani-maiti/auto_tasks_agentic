import requests
from bs4 import BeautifulSoup
import re

# Try to get gold price from Investing.com
url = "https://www.investing.com/commodities/gold"
try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Look for price in the page
        price_element = soup.find('span', {'data-test': 'last-price'})
        if price_element:
            price = price_element.text.strip()
            print(f"Gold price: {price}")
        else:
            # Try alternative method
            price_elements = soup.find_all('span', class_=re.compile(r'.*price.*', re.IGNORECASE))
            if price_elements:
                print(f"Gold price: {price_elements[0].text.strip()}")
            else:
                print("Could not find price element")
    else:
        print(f"Failed to retrieve page: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

# Try a different approach using a financial API
try:
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=gold&vs_currencies=usd"
    api_response = requests.get(api_url)
    if api_response.status_code == 200:
        data = api_response.json()
        if 'gold' in data and 'usd' in data['gold']:
            print(f"Gold price: ${data['gold']['usd']}")
        else:
            print("Could not find gold price in API response")
    else:
        print(f"API request failed: {api_response.status_code}")
except Exception as e:
    print(f"API error: {e}")