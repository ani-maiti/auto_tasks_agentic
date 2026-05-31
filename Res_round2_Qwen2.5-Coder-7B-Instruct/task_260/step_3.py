import json

with open('attribute_frequencies.txt', 'r') as f:
    lines = f.readlines()

attribute_dict = {}
for line in lines:
    count, attr = line.strip().split()
    attribute_dict[attr] = int(count)

report = json.dumps(attribute_dict, indent=4)
print(report)