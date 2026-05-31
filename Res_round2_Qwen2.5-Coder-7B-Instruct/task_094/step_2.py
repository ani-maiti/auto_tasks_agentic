import json

response = json.loads('{"tag_name": "v20.10.7"}')
print(response['tag_name'])