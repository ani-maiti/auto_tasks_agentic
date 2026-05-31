import json
from collections import defaultdict

# Read the list of XML files
with open('xml_files.txt', 'r') as file:
    xml_files = file.read().splitlines()

attributes = defaultdict(int)

for xml_file in xml_files:
    with open(xml_file, 'r') as file:
        content = file.read()
        start_index = 0
        while True:
            start_index = content.find(' ', start_index)
            if start_index == -1:
                break
            end_index = content.find('"', start_index + 1)
            if end_index != -1:
                attribute_name = content[start_index + 1:end_index]
                attributes[attribute_name] += 1
                start_index = end_index + 1

report = dict(attributes)
print(json.dumps(report, indent=4))