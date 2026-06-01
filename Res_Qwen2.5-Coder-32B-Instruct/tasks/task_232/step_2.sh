echo "jq is not installed. Installing jq..."
sudo apt-get update && sudo apt-get install -y jq
echo "jq installed. Retrieving data again..."
curl -s https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1 | jq '.[] | {name: .name, symbol: .symbol, market_cap_rank: .market_cap_rank, current_price: .current_price}' > crypto_data.json
echo "Data retrieved and saved to crypto_data.json"