import json

print("Parsing the joke...")
joke_data = json.loads('''{"type":"general","setup":"What's the best thing about elevator jokes?","punchline":"They work on so many levels.","id":269}''')
print(f"Setup: {joke_data['setup']}")
print(f"Punchline: {joke_data['punchline']}")