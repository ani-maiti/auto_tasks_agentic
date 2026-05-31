import requests

url = 'https://opentdb.com/api.php?amount=1&type=trivia'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data['response_code'] == 0:
        question = data['results'][0]['question']
        answer = data['results'][0]['correct_answer']
        print(f"Question: {question}\nAnswer: {answer}")
    else:
        print(f"Failed to retrieve trivia question: Response code {data['response_code']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")