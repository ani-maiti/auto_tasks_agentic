import requests
import json

# Try a different approach using a commodity price API
try:
    # Using a free commodity API
    api_url = "https://api.freegeoip.app/json/"
    response = requests.get(api_url)
    
    # If that fails, try a direct gold price API
    gold_api_url = "https://api.gemini.com/v1/pubticker/XAUUSD"
    response = requests.get(gold_api_url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Gold price from Gemini API: {data}")
    else:
        # Try another source
        alt_api = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=YOUR_API_KEY"
        print("Trying alternative API...")
        
except Exception as e:
    print(f"API error: {e}")

# Let's try a simple web scraping approach with a known working site
try:
    # Try goldprice.org directly
    gp_url = "https://www.goldprice.org/"
    response = requests.get(gp_url, timeout=10)
    
    if response.status_code == 200:
        content = response.text
        # Look for price in the HTML
        import re
        price_match = re.search(r'Gold Price.*?(\$[\d,]+\.?\d*)', content, re.IGNORECASE)
        if price_match:
            print(f"Gold price found: {price_match.group(1)}")
        else:
            print("No price match found in content")
    else:
        print(f"Failed to get goldprice.org: {response.status_code}")
        
except Exception as e:
    print(f"Error accessing goldprice.org: {e}")

# Final attempt with a different strategy
try:
    # Try to get the current price from a simple commodity tracker
    simple_url = "https://www.cmegroup.com/markets/metals Precious/gold.html"
    response = requests.get(simple_url, timeout=10)
    
    if response.status_code == 200:
        print("Successfully accessed CME Group page")
        # Extract price information
        import re
        price_pattern = r'[\$][\d,]+\.?\d*'
        prices = re.findall(price_pattern, response.text)
        if prices:
            print(f"Found prices: {prices}")
        else:
            print("No price patterns found")
    else:
        print(f"CME Group access failed: {response.status_code}")
        
except Exception as e:
    print(f"Error with CME Group: {e}")