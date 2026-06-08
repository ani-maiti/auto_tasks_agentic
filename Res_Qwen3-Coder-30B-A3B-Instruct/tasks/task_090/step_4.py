import requests
from bs4 import BeautifulSoup
import re

# Try a different approach - use a known working gold price website
url = "https://www.investing.com/commodities/gold"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for price elements
        price_elements = soup.find_all(['span', 'div'], class_=re.compile(r'price|last', re.IGNORECASE))
        
        for element in price_elements[:10]:  # Check first 10 elements
            text = element.get_text().strip()
            if re.search(r'\$\d+\.?\d*', text):
                print(f"Found price: {text}")
                break
        else:
            # Try to find any numeric price pattern
            content = response.text
            price_pattern = r'[\$][\d,]+\.?\d*'
            prices = re.findall(price_pattern, content)
            if prices:
                print(f"Found prices: {prices}")
            else:
                print("No price found in the page")
                
    else:
        print(f"HTTP Error: {response.status_code}")
        
except Exception as e:
    print(f"Error: {e}")

# Try a simple curl command to see if we can get data
print("Attempting to get gold price from a simple API...")
try:
    # Using a different API endpoint
    api_url = "https://api.coinbase.com/v2/prices/XAU-USD/spot"
    response = requests.get(api_url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Coinbase API response: {data}")
    else:
        print(f"Coinbase API failed with status: {response.status_code}")
        
except Exception as e:
    print(f"Coinbase API error: {e}")