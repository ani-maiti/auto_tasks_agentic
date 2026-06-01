echo "Jq is not installed. Downloading weather data using curl..."
curl -s "https://api.open-meteo.com/v1/forecast?latitude=35.6828&longitude=139.6915&current_weather=true"