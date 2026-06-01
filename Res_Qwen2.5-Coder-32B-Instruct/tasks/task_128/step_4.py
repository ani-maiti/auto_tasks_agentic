import json

response = '{"facts":["One survey reports that 33% of dog owners admit they talk to their dogs on the phone or leave messages on answering machines while they are away.."],"success":true}'
data = json.loads(response)
print("Random Dog Fact:", data['facts'][0])