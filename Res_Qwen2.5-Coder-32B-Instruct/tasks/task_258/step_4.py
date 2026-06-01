import json

with open('repos.json', 'r') as file:
    data = json.load(file)

languages = {}
for repo in data['items']:
    language = repo.get('language', 'Unknown')
    if language in languages:
        languages[language] += 1
    else:
        languages[language] = 1

with open('language_stats.json', 'w') as file:
    json.dump(languages, file, indent=4)

print("Language statistics saved to language_stats.json")
print(languages)