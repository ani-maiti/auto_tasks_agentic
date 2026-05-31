import json

response = '{"tag_name": "v20.10.7"}'
data = json.loads(response)
print(data['tag_name'])