# Step 10: Define the target URL again
target_url = "https://docs.python.org/3/"

# Step 11: Re-run the fetch and parse function
initial_page = fetch_and_parse_page(target_url)
page_data.append(initial_page)

# Step 12: Print the number of collected pages so far
print(f"Collected {len(page_data)} pages.")