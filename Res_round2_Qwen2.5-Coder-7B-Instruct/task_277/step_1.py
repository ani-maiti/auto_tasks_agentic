import requests
from bs4 import BeautifulSoup
import json

# Step 1: Retrieve the list of largest cities in each US state
url = "https://en.wikipedia.org/wiki/List_of_largest_cities_in_the_United_States"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

cities_by_state = {}

table = soup.find('table', {'class': 'wikitable sortable'})
rows = table.find_all('tr')[1:]  # Skip header row

for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0:
        state = cells[0].text.strip()
        city = cells[2].text.strip()
        population = int(cells[3].text.replace(',', '').strip())
        
        if state not in cities_by_state:
            cities_by_state[state] = []
        
        cities_by_state[state].append((city, population))

# Print the first few entries to verify
print(json.dumps(cities_by_state, indent=2)[:500])
```

This code retrieves the list of largest cities in each US state from a Wikipedia page and stores it in a dictionary. The first few entries are printed to verify the data.