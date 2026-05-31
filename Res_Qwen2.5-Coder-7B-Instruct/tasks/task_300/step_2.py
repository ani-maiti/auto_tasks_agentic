import xml.etree.ElementTree as ET
from collections import defaultdict

# Step 2: Infer schemas from observed structures
schemas = defaultdict(list)

for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root_tag = tree.getroot().tag
    schema = (root_tag, [child.tag for child in tree.iter()])

    schemas[schema].append(xml_file)

print(f"Inferred {len(schemas)} unique schemas.")