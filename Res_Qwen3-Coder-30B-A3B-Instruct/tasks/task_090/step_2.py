import requests

# Try a more reliable gold price source
urls = [
    "https://www.goldprice.org/",
    "https://www.livebitcoinprice.com/gold-price/",
    "https://www.investing.com/commodities/gold-historical-data"
]

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"Successfully accessed: {url}")
            # Look for price pattern in the content
            content = response.text.lower()
            if 'gold' in content and 'price' in content:
                print("Found gold price information in page")
                break
    except Exception as e:
        print(f"Failed to access {url}: {e}")
        continue

# Try Yahoo Finance API approach
try:
    yf_url = "https://query1.finance.yahoo.com/v8/finance/chart/XAU-USD"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(yf_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Yahoo Finance data retrieved successfully")
        print(f"Current price data: {data}")
    else:
        print(f"Yahoo Finance request failed: {response.status_code}")
except Exception as e:
    print(f"Yahoo Finance error: {e}")