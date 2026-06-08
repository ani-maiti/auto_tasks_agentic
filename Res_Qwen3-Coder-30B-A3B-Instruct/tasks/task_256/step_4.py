import os
import json
import re
from collections import defaultdict

# Find all text files
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

# Read content from all files and extract sentences
file_sentences = defaultdict(list)
sentence_counts = defaultdict(int)
all_sentences = []

for file_path in text_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Split into sentences using regex
            sentences = re.split(r'[.!?]+', content)
            sentences = [s.strip() for s in sentences if s.strip()]
            
            file_sentences[file_path] = sentences
            all_sentences.extend(sentences)
            
            # Count sentence occurrences
            for sentence in sentences:
                sentence_counts[sentence] += 1
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Find duplicated sentences
duplicated_sentences = {sentence: count for sentence, count in sentence_counts.items() if count > 1}

print(f"Total sentences found: {len(all_sentences)}")
print(f"Unique sentences: {len(sentence_counts)}")
print(f"Duplicated sentences: {len(duplicated_sentences)}")

# Create report structure
report = {
    "total_text_files": len(text_files),
    "total_sentences": len(all_sentences),
    "unique_sentences": len(sentence_counts),
    "duplicated_sentences_count": len(duplicated_sentences),
    "duplicated_sentences": {}
}

# Add details about duplicated sentences
for sentence, count in duplicated_sentences.items():
    files_containing = []
    for file_path, sentences in file_sentences.items():
        if sentence in sentences:
            files_containing.append(file_path)
    
    report["duplicated_sentences"][sentence] = {
        "count": count,
        "files": files_containing
    }

# Save to JSON file
with open('duplication_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Report saved to duplication_report.json")