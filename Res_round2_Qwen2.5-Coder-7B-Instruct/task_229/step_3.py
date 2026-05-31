import csv

# Step 2: Extract company names from the titles and URLs
def extract_companies(text):
    # Simple regex pattern to find words that look like company names
    return re.findall(r'\b[A-Z][a-z]*\b', text)

companies = []

with open('hacker_news_stories.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for _, url in reader:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        story_text = soup.find('div', id='body').text
        companies.extend(extract_companies(story_text))

# Count the frequency of each company name
company_counts = Counter(companies)

# Save the ranked report to a CSV file
with open('company_report.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company', 'Count'])
    for company, count in company_counts.most_common():
        writer.writerow([company, count])

print("Ranked report saved to company_report.csv")