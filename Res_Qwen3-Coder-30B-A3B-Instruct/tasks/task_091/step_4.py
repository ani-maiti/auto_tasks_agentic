import requests
import json

# Try a different approach using a known working commodity price API
# Let's try the Alpha Vantage API which has a free tier
# But first, let's try a simple web scraping approach with a more reliable site

# Try goldprice.org which often works for precious metal prices
try:
    response = requests.get("https://www.goldprice.org/", timeout=10)
    if response.status_code == 200:
        print("Successfully accessed goldprice.org")
        content = response.text
        
        # Look for silver price specifically
        if "silver" in content.lower():
            print("Found silver content in goldprice.org")
            
            # Extract price using simple string operations
            silver_index = content.lower().find("silver")
            if silver_index != -1:
                # Look for price nearby
                start_pos = max(0, silver_index - 100)
                end_pos = min(len(content), silver_index + 200)
                context = content[start_pos:end_pos]
                print("Context around silver:", context[:100])
        else:
            print("No silver reference found")
    else:
        print(f"Failed to access goldprice.org: {response.status_code}")
        
except Exception as e:
    print(f"Error with goldprice.org: {e}")

# Try a simple HTTP GET to a known working site
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print("Bitcoin price data retrieved:", data['bpi']['USD']['rate'])
    else:
        print("Failed to get Bitcoin data")
except Exception as e:
    print(f"Bitcoin API error: {e}")