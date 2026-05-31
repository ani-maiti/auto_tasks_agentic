import requests

url = 'https://www.trivia-api.com/questions?limit=1&category=Entertainment'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data:
        question = data[0]['question']
        answer = data[0]['answers'][0]
        print(f"Question: {question}\nAnswer: {answer}")
    else:
        print("No data received")
else:
    print(f"Failed to retrieve data: {response.status_code}")