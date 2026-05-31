import os
import xml.etree.ElementTree as ET
from collections import Counter

# List all XML files in the current directory and subdirectories
xml_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xml'):
            xml_files.append(os.path.join(root, file))

root_elements = []

for file_path in xml_files:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        root_elements.append(root.tag)
    except ET.ParseError:
        print(f"Failed to parse {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

counter = Counter(root_elements)
most_common_root = counter.most_common(1)

print(f"The most common root element is: {most_common_root[0][0]}")