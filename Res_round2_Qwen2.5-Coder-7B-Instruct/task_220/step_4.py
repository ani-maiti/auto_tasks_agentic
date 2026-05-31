import json

with open('module_frequency.json', 'w') as file:
    json.dump(dict(sorted_modules), file, indent=4)

print("Frequency table saved to module_frequency.json")