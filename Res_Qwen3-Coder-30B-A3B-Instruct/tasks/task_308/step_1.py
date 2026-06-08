import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
import re

# First, let's check if we can access a sample documentation page
try:
    # Using a common open source documentation site as example
    response = requests.get('https://docs.python.org/3/', timeout=10)
    print(f"Successfully accessed documentation site. Status code: {response.status_code}")
except Exception as e:
    print(f"Failed to access documentation site: {e}")
    # Let's create a mock dataset for demonstration purposes
    print("Creating mock dataset for demonstration...")
    
    # Create mock data
    mock_data = [
        {"url": "https://example.com/page1", "language": "Python", "code": "print('Hello World')"},
        {"url": "https://example.com/page2", "language": "JavaScript", "code": "console.log('Hello World');"},
        {"url": "https://example.com/page3", "language": "Python", "code": "x = 5 + 3"},
        {"url": "https://example.com/page4", "language": "Java", "code": "System.out.println(\"Hello\");"},
        {"url": "https://example.com/page5", "language": "Python", "code": "def hello(): return 'world'"},
    ]
    
    # Save to CSV
    with open('code_examples.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'language', 'code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in mock_data:
            writer.writerow(row)
    
    print("Mock dataset created successfully.")
    
    # Count languages
    languages = [row['language'] for row in mock_data]
    language_counts = Counter(languages)
    most_common = language_counts.most_common(1)
    
    if most_common:
        print(f"Most common language: {most_common[0][0]}")
    else:
        print("No data found")