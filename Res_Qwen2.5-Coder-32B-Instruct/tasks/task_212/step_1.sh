echo "Searching for a public API for exchange rates..."
curl -s https://api.exchangerate-api.com/v4/latest/USD | jq .