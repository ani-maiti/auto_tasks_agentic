import requests
import csv
import pandas as pd

# First, let's try to fetch data from CoinGecko API which is a popular public crypto API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1,
    'sparkline': False
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    print(f"Successfully fetched data for {len(data)} coins")
    
    # Extract relevant fields
    coins_data = []
    for coin in data:
        coin_data = {
            'id': coin['id'],
            'name': coin['name'],
            'symbol': coin['symbol'],
            'current_price': coin['current_price'],
            'market_cap': coin['market_cap'],
            'market_cap_rank': coin['market_cap_rank'],
            'total_volume': coin['total_volume']
        }
        coins_data.append(coin_data)
    
    # Save to CSV
    df = pd.DataFrame(coins_data)
    df.to_csv('crypto_prices.csv', index=False)
    print("Data saved to crypto_prices.csv")
    
    # Print top 10 coins
    print("\nTop 10 Cryptocurrencies by Market Cap:")
    top_10 = df.head(10)
    for index, row in top_10.iterrows():
        print(f"{row['market_cap_rank']}. {row['name']} ({row['symbol'].upper()}) - ${row['current_price']:,.2f}")
        
except Exception as e:
    print(f"Error: {e}")
    print("Trying alternative API...")
    
    # Try another approach with a different API
    alt_url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing/latest"
    headers = {
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(alt_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("Alternative API worked")
        else:
            print("Both APIs failed")
    except Exception as alt_e:
        print(f"Alternative API also failed: {alt_e}")