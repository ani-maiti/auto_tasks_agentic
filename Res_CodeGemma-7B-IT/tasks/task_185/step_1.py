import glob
import xml.etree.ElementTree as ET

for filename in glob.glob("*.xml"):
    try:
        tree = ET.parse(filename)
        print(f"{filename}: Valid XML")
    except Exception as e:
        print(f"{filename}: Invalid XML ({e})")