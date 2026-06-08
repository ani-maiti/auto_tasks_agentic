import requests

# Try another API to get a different type of question
url = "https://jservice.io/api/random"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if isinstance(data, list):
        question = data[0]["question"]
        print(question)
    else:
        question = data["question"]
        print(question)
else:
    print("API request failed")