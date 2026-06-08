import xml.etree.ElementTree as ET
import os

def is_valid_xml(file_path):
    try:
        ET.parse(file_path)
        return True
    except ET.ParseError:
        return False
    except Exception:
        return False

# Find all XML files and check their validity
xml_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xml'):
            xml_files.append(os.path.join(root, file))

print(f"Found {len(xml_files)} XML files:")
for file in xml_files:
    valid = is_valid_xml(file)
    status = "Valid" if valid else "Invalid"
    print(f"{file}: {status}")