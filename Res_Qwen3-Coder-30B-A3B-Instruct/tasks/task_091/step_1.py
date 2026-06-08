import requests
from bs4 import BeautifulSoup

# Try to get silver price from a financial website
url = "https://www.investing.com/commodities/silver"
try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Look for price elements
        price_element = soup.find('span', {'data-test': 'last-price'})
        if price_element:
            print(price_element.text.strip())
        else:
            # Try alternative method
            price_elements = soup.find_all('span', class_='text-2xl')
            if price_elements:
                print(price_elements[0].text.strip())
            else:
                print("Price not found")
    else:
        print(f"Failed to retrieve data: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")