from lxml import etree

# Step 2: Infer schemas from observed structures
schemas = {}
for xml_file in xml_files:
    tree = etree.parse(xml_file)
    root_tag = tree.getroot().tag
    if root_tag not in schemas:
        schemas[root_tag] = []
    schemas[root_tag].append(tree)

# Print the number of unique root tags found
print(f"Found {len(schemas)} unique root tags.")