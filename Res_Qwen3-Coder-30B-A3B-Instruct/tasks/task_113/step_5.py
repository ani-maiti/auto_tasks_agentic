import re
import requests

url = "https://www.kernel.org/"
response = requests.get(url)
content = response.text
title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
if title_match:
    print(title_match.group(1))
else:
    print("Title not found")