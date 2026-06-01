echo "Parsing weather data for London..."
curl -s "https://wttr.in/London?format=j1" | jq '.current_condition[0].temp_C + "°C, " + .current_condition[0].weatherDesc[0].value'