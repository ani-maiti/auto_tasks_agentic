import requests
import json

# Try using a different commodity price source
# Using a free API that might work without authentication
url = "https://api.freegeoip.app/json/?apikey=freegeoip.app-api-key"

# Actually, let's try a more reliable approach with a known working commodity API
# https://www.worldtradingdata.com/ has a free tier but requires registration

# Let's try a simple curl approach to see what's available
try:
    # First check if we can access a basic commodity site
    response = requests.get("https://www.cmegroup.com/markets/metals/silver.html", timeout=10)
    if response.status_code == 200:
        print("Successfully accessed CME group silver page")
        # Extract price information from the page
        content = response.text
        # Look for common price patterns
        if "USD" in content and "per" in content:
            print("Found price-related content")
        else:
            print("No obvious price content found")
    else:
        print(f"Failed to access CME site: {response.status_code}")
        
except Exception as e:
    print(f"Error accessing CME site: {e}")

# Try another approach - Yahoo Finance API
try:
    response = requests.get("https://query1.finance.yahoo.com/v8/finance/chart/SILVER%21?region=US&lang=en-US&includePrePost=false&interval=2m&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance", timeout=10)
    if response.status_code == 200:
        data = response.json()
        print("Yahoo Finance data retrieved successfully")
        print(json.dumps(data, indent=2))
    else:
        print(f"Yahoo Finance error: {response.status_code}")
except Exception as e:
    print(f"Yahoo Finance error: {e}")