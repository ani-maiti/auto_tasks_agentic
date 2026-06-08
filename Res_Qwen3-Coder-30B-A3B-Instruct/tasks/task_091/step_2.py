import requests

# Try a different approach with a commodity price API
url = "https://api.polygon.io/v2/aggs/ticker/XA%3ASLV/range/1/day/2023-01-01/2023-01-02?adjusted=true&sort=asc&limit=120&apiKey=YOUR_API_KEY"

# Since we can't use an API key, let's try a free alternative
url = "https://www.goldprice.org/silver-price"

try:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        print("Successfully retrieved page")
        # Just check if we can access the content
        print(f"Page length: {len(response.content)}")
    else:
        print(f"Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")