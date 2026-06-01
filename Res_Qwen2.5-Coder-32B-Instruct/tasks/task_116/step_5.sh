echo "Invalid API key. Please provide a valid API key for OpenWeatherMap."
read -p "Enter your OpenWeatherMap API key: " api_key
curl "https://api.openweathermap.org/data/2.5/weather?q=Sydney&appid=$api_key"