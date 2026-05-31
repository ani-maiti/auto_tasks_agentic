import requests

url = "https://www.bloomberg.com/quote/SLV:COM"

response = requests.get(url)

if response.status_code == 200:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("div", class_="price").text
    print(f"Current price of silver: {price}")
else:
    print(f"Error retrieving silver price: {response.status_code}")