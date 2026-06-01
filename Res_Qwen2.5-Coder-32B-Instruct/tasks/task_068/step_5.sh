echo "Printing jokes..."
curl -s https://official-joke-api.appspot.com/random_joke | jq -r '.setup + " " + .punchline'
curl -s https://official-joke-api.appspot.com/random_joke | jq -r '.setup + " " + .punchline'
curl -s https://official-joke-api.appspot.com/random_joke | jq -r '.setup + " " + .punchline'