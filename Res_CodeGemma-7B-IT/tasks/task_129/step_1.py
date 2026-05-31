import requests

url = "https://opentdb.com/api.php?amount=1&type=boolean"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    question = data["results"][0]["question"]
    answer = data["results"][0]["correct_answer"]
    print(f"Question: {question}")
    print(f"Answer: {answer}")
else:
    print("Error retrieving trivia question.")