import os
import json
import re
from collections import Counter
from datetime import datetime

def extract_entities(text):
    """Extract various types of entities from text"""
    entities = {
        'emails': [],
        'urls': [],
        'dates': [],
        'phone_numbers': [],
        'numbers': []
    }
    
    # Email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    entities['emails'] = re.findall(email_pattern, text)
    
    # URL pattern
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    entities['urls'] = re.findall(url_pattern, text)
    
    # Date patterns (YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY)
    date_patterns = [
        r'\b\d{4}-\d{2}-\d{2}\b',  # YYYY-MM-DD
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # MM/DD/YYYY or DD/MM/YYYY
        r'\b\d{2}-\d{2}-\d{4}\b'   # MM-DD-YYYY
    ]
    
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        entities['dates'].extend(matches)
    
    # Phone number patterns
    phone_patterns = [
        r'\b\d{3}-\d{3}-\d{4}\b',  # XXX-XXX-XXXX
        r'\(\d{3}\)\s\d{3}-\d{4}',  # (XXX) XXX-XXXX
        r'\b\d{3}\.\d{3}\.\d{4}\b'  # XXX.XXX.XXXX
    ]
    
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        entities['phone_numbers'].extend(matches)
    
    # Number pattern
    number_pattern = r'\b\d+(?:\.\d+)?\b'
    entities['numbers'] = re.findall(number_pattern, text)
    
    return entities

def process_text_files(directory):
    """Find all text files and extract entities"""
    all_entities = {}
    total_entities = Counter()
    
    # Find all .txt files
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    
    print(f"Found {len(txt_files)} text files")
    
    for filepath in txt_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            entities = extract_entities(content)
            
            # Store entities for this file
            all_entities[filepath] = entities
            
            # Count total occurrences of each entity type
            for entity_type, values in entities.items():
                total_entities[entity_type] += len(values)
                
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    
    return all_entities, total_entities

# Process text files
all_entities, total_entities = process_text_files("/tmp")

# Save results to JSON
with open('entity_inventory.json', 'w') as f:
    json.dump(all_entities, f, indent=2)

print("Entity inventory saved to entity_inventory.json")
print("Total entities by type:")
for entity_type, count in total_entities.items():
    print(f"  {entity_type}: {count}")

# Find most common entity type
if total_entities:
    most_common = total_entities.most_common(1)[0]
    print(f"\nMost common entity type: {most_common[0]} with {most_common[1]} occurrences")
else:
    print("\nNo entities found")