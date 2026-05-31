import os
import xml.etree.ElementTree as ET
from collections import defaultdict

# Get all XML files in the current directory
xml_files = [f for f in os.listdir('.') if f.endswith('.xml')]

# Initialize dictionary to store attribute frequencies
attribute_frequencies = defaultdict(int)

# Iterate over XML files
for xml_file in xml_files:
    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract attribute names and frequencies
    for element in root.iter():
        for attribute in element.attrib:
            attribute_frequencies[attribute] += 1

# Create a report dictionary
report = {
    'total_files': len(xml_files),
    'attributes': attribute_frequencies
}

# Save report to JSON file
import json
with open('attribute_frequencies.json', 'w') as f:
    json.dump(report, f)