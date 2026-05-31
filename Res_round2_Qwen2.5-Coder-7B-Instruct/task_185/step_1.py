import os
import xml.etree.ElementTree as ET

def check_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print(f"{file_path} is valid XML")
    except ET.ParseError:
        print(f"{file_path} is not valid XML")

def find_and_check_xml_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                check_xml(os.path.join(root, file))

# Replace 'path/to/directory' with the actual directory path you want to scan
find_and_check_xml_files('path/to/directory')