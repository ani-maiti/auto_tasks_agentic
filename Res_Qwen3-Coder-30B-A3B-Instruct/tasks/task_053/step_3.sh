# Let's try using a different weather API that doesn't require an API key
curl -s "https://wttr.in/Tokyo?format=%t" | tr -d '\n'
echo ""