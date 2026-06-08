import urllib.request
import re

# Fetch the Wikipedia page for Linux
url = "https://en.wikipedia.org/wiki/Linux"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    
    # Extract title using regex
    title_match = re.search(r'<title>(.*?) - Wikipedia</title>', html)
    
    if title_match:
        print(title_match.group(1))
    else:
        print("Title not found")
        
except Exception as e:
    print(f"Error: {e}")