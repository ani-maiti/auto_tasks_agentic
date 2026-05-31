curl -s "http://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=YOUR_API_KEY&units=metric" | jq '.main.temp'
```

Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key. This command uses `curl` to fetch the weather data and `jq` to parse and extract the temperature. Make sure you have `jq` installed on your system. If not, you can install it using your package manager.