import os
import xml.etree.ElementTree as ET
from collections import defaultdict

# Step 1: Discover all XML files in the current directory and its subdirectories
xml_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xml'):
            xml_files.append(os.path.join(root, file))

print(f"Found {len(xml_files)} XML files.")

# Step 2: Infer schemas from observed structures
schemas = defaultdict(list)

for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root_tag = tree.getroot().tag
    schema = (root_tag, [child.tag for child in tree.iter()])

    schemas[schema].append(xml_file)

print(f"Inferred {len(schemas)} unique schemas.")