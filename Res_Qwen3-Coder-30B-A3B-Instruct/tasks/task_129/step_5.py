import requests

# Final attempt with a different category
url = "https://opentdb.com/api.php?amount=1&category=18&type=multiple"
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