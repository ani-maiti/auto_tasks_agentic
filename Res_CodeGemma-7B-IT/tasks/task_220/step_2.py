# Save the frequency table to a JSON file
with open('module_frequencies.json', 'w') as f:
    json.dump(sorted_modules, f)