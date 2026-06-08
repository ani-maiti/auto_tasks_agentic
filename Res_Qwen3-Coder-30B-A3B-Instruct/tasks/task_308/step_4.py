import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
import re
from urllib.parse import urljoin, urlparse
import time

# We'll work with the Python documentation as our target
base_url = "https://docs.python.org/3/"
start_url = "https://docs.python.org/3/"

# Function to extract code examples from a page
def extract_code_examples(soup, url):
    examples = []
    
    # Look for code blocks in various formats
    code_selectors = [
        'pre',
        'code',
        '.highlight',
        '.literal-block'
    ]
    
    for selector in code_selectors:
        elements = soup.select(selector)
        for element in elements:
            # Get text content
            code_text = element.get_text().strip()
            
            # Skip very short snippets
            if len(code_text) < 10:
                continue
                
            # Try to detect language from context or heuristics
            language = classify_language(code_text)
            
            if language:
                examples.append({
                    'url': url,
                    'language': language,
                    'code': code_text[:500]  # Limit length
                })
    
    return examples

# Simple language classifier based on syntax patterns
def classify_language(code_text):
    code_text_lower = code_text.lower()
    
    if re.search(r'\b(print|def|if|for|while|import|from)\b', code_text_lower):
        return "Python"
    elif re.search(r'\b(console\.log|var|let|const|function)\b', code_text_lower):
        return "JavaScript"
    elif re.search(r'\b(System\.out|public|class|import)\b', code_text_lower):
        return "Java"
    elif re.search(r'\b(printf|include|main|void)\b', code_text_lower):
        return "C/C++"
    elif re.search(r'\b(println|val|var)\b', code_text_lower):
        return "Scala"
    elif re.search(r'\b(puts|require|def)\b', code_text_lower):
        return "Ruby"
    elif re.search(r'\b(println|defn|ns)\b', code_text_lower):
        return "Clojure"
    else:
        # Default to Python if we can't determine
        return "Python"

# Function to get all links from a page
def get_links(soup, base_url):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        full_url = urljoin(base_url, href)
        # Only include URLs from the same domain
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            links.append(full_url)
    return list(set(links))  # Remove duplicates

# Main crawling function
def crawl_and_extract(max_pages=50):  # Reduced for demo purposes
    visited = set()
    all_examples = []
    pages_crawled = 0
    
    # Start with the main page
    urls_to_visit = [start_url]
    
    while urls_to_visit and pages_crawled < max_pages:
        current_url = urls_to_visit.pop(0)
        
        if current_url in visited:
            continue
            
        try:
            print(f"Crawling: {current_url}")
            response = requests.get(current_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            visited.add(current_url)
            pages_crawled += 1
            
            # Extract code examples
            examples = extract_code_examples(soup, current_url)
            all_examples.extend(examples)
            
            # Get new links to visit
            new_links = get_links(soup, base_url)
            urls_to_visit.extend([link for link in new_links if link not in visited])
            
            # Be respectful to the server
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")
            continue
    
    return all_examples

# Run the crawler
print("Starting to crawl documentation site...")
examples = crawl_and_extract(max_pages=20)  # Small number for demo

# Save to CSV
if examples:
    with open('code_examples.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'language', 'code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for example in examples:
            writer.writerow(example)
    
    print("Saved code examples to CSV file")
    
    # Generate report
    languages = [example['language'] for example in examples]
    language_counts = Counter(languages)
    
    print("\n--- Report ---")
    print("Total examples collected: " + str(len(examples)))