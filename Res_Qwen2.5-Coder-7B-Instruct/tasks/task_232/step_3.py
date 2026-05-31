import requests
import pandas as pd

# Define the URL for the CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price"

# Define the parameters for the API request
params = {
    'ids': 'bitcoin,ethereum,litecoin,dogecoin,solana,tether,cardano,polkadot,chainlink,uniswap',
    'vs_currencies': 'usd'
}

# Send the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(list(data.items()), columns=['Coin', 'Price'])
    
    # Sort the DataFrame by price in descending order
    df_sorted = df.sort_values(by='Price', ascending=False)
    
    # Save the DataFrame to a CSV file
    df_sorted.to_csv('crypto_prices.csv', index=False)
    
    # Print the top 10 coins
    print(df_sorted.head(10))
else:
    print(f"Failed to retrieve data: {response.status_code}")