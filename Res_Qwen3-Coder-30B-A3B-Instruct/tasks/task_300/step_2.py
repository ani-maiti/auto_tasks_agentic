import os
import xml.etree.ElementTree as ET
from collections import defaultdict, Counter
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re

# Find all XML files
xml_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.xml'):
            xml_files.append(os.path.join(root, file))

print(f"Found {len(xml_files)} XML files")
```