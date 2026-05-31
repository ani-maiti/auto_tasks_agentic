import os
import xml.etree.ElementTree as ET

# Get all XML files in the current directory
xml_files = [f for f in os.listdir('.') if f.endswith('.xml')]

# Initialize data structures to store information
root_elements = {}
validation_results = {}

# Iterate over each XML file
for xml_file in xml_files:
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Get the root element name
        root_element = root.tag

        # Validate the XML file
        validation_results[xml_file] = "Valid"
        try:
            tree.getroot()
        except Exception as e:
            validation_results[xml_file] = f"Invalid: {e}"

        # Add the root element to the list
        if root_element not in root_elements:
            root_elements[root_element] = 0
        root_elements[root_element] += 1

    except Exception as e:
        validation_results[xml_file] = f"Error parsing XML file: {e}"

# Print the summary report
print("XML Summary Report:")
for xml_file, result in validation_results.items():
    print(f"\t{xml_file}: {result}")

# Print the most common root element
most_common_root = max(root_elements, key=root_elements.get)
print(f"\nMost Common Root Element: {most_common_root}")