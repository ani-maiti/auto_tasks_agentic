import requests
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL verification warning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

response = requests.get('https://api.quotable.io/random', verify=False)
if response.status_code == 200:
    quote = response.json()
    print(quote['content'])
else:
    print("Failed to retrieve quote")