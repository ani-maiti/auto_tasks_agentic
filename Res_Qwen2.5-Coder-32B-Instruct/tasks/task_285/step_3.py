import tldextract
from collections import defaultdict
import re

def extract_domain_and_keywords(stories):
    extracted_data = []
    for story in stories:
        domain = tldextract.extract(story.get('url', '')).domain
        title = story.get('title', '')
        score = story.get('score', 0)
        # Simple keyword extraction using regex to find words
        keywords = re.findall(r'\b\w+\b', title.lower())
        extracted_data.append({
            'domain': domain,
            'keywords': keywords,
            'score': score
        })
    return extracted_data

extracted_data = extract_domain_and_keywords(stories)
print("Extracted data length:", len(extracted_data))