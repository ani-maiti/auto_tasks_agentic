import os
import re
from collections import defaultdict

def find_text_files(directory="."):
    """Find all text files in the given directory recursively."""
    text_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                text_files.append(os.path.join(root, file))
    return text_files

def read_file_content(filepath):
    """Read content of a file and return as list of paragraphs."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Split by double newlines to get paragraphs
            paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
            return paragraphs
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def find_duplicates(text_files):
    """Find duplicated paragraphs across all text files."""
    paragraph_to_files = defaultdict(list)
    all_paragraphs = []
    
    # Read all files and collect paragraphs
    for filepath in text_files:
        paragraphs = read_file_content(filepath)
        for para in paragraphs:
            paragraph_to_files[para].append(filepath)
            all_paragraphs.append((para, filepath))
    
    # Find duplicates (paragraphs appearing in more than one file)
    duplicates = {}
    for para, files in paragraph_to_files.items():
        if len(files) > 1:
            duplicates[para] = files
    
    return duplicates

def generate_report(duplicates):
    """Generate a report of duplicates."""
    if not duplicates:
        print("No duplicates found.")
        return
    
    print("Duplicate Paragraph Report:")
    print("=" * 50)
    
    # Sort by number of occurrences (descending)
    sorted_duplicates = sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True)
    
    for para, files in sorted_duplicates:
        print(f"\nParagraph: {para[:100]}...")
        print(f"Occurrences in files: {len(files)}")
        for file in files:
            print(f"  - {file}")

def find_largest_duplicate_block(duplicates):
    """Find and return the largest duplicated block."""
    if not duplicates:
        return None
    
    largest_block = max(duplicates.keys(), key=len)
    return largest_block

# Main execution
text_files = find_text_files()
print(f"Found {len(text_files)} text files.")

duplicates = find_duplicates(text_files)
generate_report(duplicates)

largest_duplicate = find_largest_duplicate_block(duplicates)
if largest_duplicate:
    print("\nLargest duplicated block:")
    print("=" * 50)
    print(largest_duplicate)
else:
    print("\nNo duplicates found to determine largest block.")