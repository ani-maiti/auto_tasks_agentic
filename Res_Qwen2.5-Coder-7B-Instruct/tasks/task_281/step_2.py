# Step 6: Initialize a list to store page data
page_data = []

# Step 7: Define a function to fetch and parse a page
def fetch_and_parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    headings = [h.text for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return {
        'url': url,
        'title': title,
        'headings': headings,
        'links': links
    }

# Step 8: Add the initial page to the list
initial_page = fetch_and_parse_page(target_url)
page_data.append(initial_page)

# Step 9: Print the number of collected pages so far
print(f"Collected {len(page_data)} pages.")