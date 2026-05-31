import requests

url = 'https://jservice.io/api/random'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data:
        question = data[0]['question']
        answer = data[0]['answer']
        print(f"Question: {question}\nAnswer: {answer}")
    else:
        print("No data received")
else:
    print(f"Failed to retrieve data: {response.status_code}")