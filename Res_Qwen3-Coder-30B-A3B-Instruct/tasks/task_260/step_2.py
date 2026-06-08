import xml.etree.ElementTree as ET
from collections import Counter
import json
import os

# Find all XML files
xml_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xml'):
            xml_files.append(os.path.join(root, file))

print(f"Found {len(xml_files)} XML files")

# Extract attributes and count frequencies
all_attributes = []

for xml_file in xml_files:
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Recursive function to get all attributes
        def get_attributes(element):
            attrs = list(element.attrib.keys())
            for child in element:
                attrs.extend(get_attributes(child))
            return attrs
        
        all_attributes.extend(get_attributes(root))
    except Exception as e:
        print(f"Error parsing {xml_file}: {e}")

# Count frequencies
attr_freq = Counter(all_attributes)

# Generate report
report = {
    "total_xml_files": len(xml_files),
    "total_unique_attributes": len(attr_freq),
    "attribute_frequencies": dict(attr_freq),
    "most_common_attributes": attr_freq.most_common(10)
}

# Save to JSON
with open('xml_attribute_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Report saved to xml_attribute_report.json")
print(f"Total unique attributes: {len(attr_freq)}")
print("Most common attributes:")
for attr, freq in attr_freq.most_common(5):
    print(f"  {attr}: {freq}")