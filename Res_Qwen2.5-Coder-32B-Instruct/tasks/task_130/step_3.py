import json

print("Parsing JSON response...")
response = '{"slip": { "id": 52, "advice": "Don\'t promise what you can\'t deliver."}}'
data = json.loads(response)
advice_message = data['slip']['advice']
print("Random advice message:", advice_message)