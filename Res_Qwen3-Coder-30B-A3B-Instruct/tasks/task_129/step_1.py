import requests

# Try to fetch a random trivia question from the Open Trivia Database API
url = "https://opentdb.com/api.php?amount=1&type=boolean"
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