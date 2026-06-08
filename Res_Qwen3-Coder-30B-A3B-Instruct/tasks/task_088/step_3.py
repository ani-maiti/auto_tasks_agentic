import urllib.request
import re

# Fetch the Wikipedia page for Python programming language
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0')

try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    
    # Extract the title using regex
    title_match = re.search(r'<title>(.*?) - Wikipedia</title>', html)
    
    if title_match:
        title = title_match.group(1)
        print(title)
    else:
        print("Title not found")
        
except Exception as e:
    print(f"Error: {e}")