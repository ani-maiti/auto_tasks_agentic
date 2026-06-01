echo "jq is not installed. Using curl to fetch weather data without jq..."
curl "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Sydney"