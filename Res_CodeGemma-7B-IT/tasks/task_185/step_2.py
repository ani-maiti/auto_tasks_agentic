import glob
import xml.etree.ElementTree as ET

for filename in glob.glob("*.xml"):
    try:
        tree = ET.parse(filename)
        print(f"{filename}: Valid XML")
    except Exception as e:
        print(f"{filename}: Invalid XML ({e})")
```

This code iterates over all files with the extension ".xml" in the current directory. For each file, it attempts to parse the file using the `xml.etree.ElementTree` library. If the parsing is successful, it prints a message stating that the file is a valid XML file. Otherwise, it prints an error message stating that the file is an invalid XML file and the reason for the error.