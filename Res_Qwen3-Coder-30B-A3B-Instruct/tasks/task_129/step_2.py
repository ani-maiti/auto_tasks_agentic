import requests

# Try a different API endpoint for variety
url = "https://opentdb.com/api.php?amount=1&type=multiple"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data["response_code"] == 0:  # Success
        question = data["results"][0]["question"]
        print(question)
    else:
        print("Failed to retrieve trivia question")
else:
    print("API request failed")