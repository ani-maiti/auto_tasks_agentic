import re
from collections import defaultdict
import json

def extract_sentences(text):
    # Split by sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    # Remove empty strings and strip whitespace
    return [s.strip() for s in sentences if s.strip()]

def get_sentence_length(sentence):
    return len(sentence)

# Collect all sentences with their file sources
all_sentences = []

# Process first few files to test
sample_files = ['./tasks/task_147/stdout_step_2.txt', './tasks/task_147/stdout_step_1.txt', './tasks/task_147/stderr_step_3.txt']

for file_path in sample_files:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            sentences = extract_sentences(content)
            for sentence in sentences:
                if sentence:  # Only add non-empty sentences
                    all_sentences.append({
                        'sentence': sentence,
                        'length': len(sentence),
                        'file': file_path
                    })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Sort by length and get top 100
all_sentences.sort(key=lambda x: x['length'], reverse=True)
top_100 = all_sentences[:100]

print(f"Found {len(all_sentences)} sentences")
print("Top 5 longest sentences:")
for i, sent in enumerate(top_100[:5]):
    print(f"{i+1}. Length: {sent['length']}, Sentence: {sent['sentence'][:100]}...")

# Save to JSON
with open('top_100_longest_sentences.json', 'w') as f:
    json.dump(top_100, f, indent=2)

print("Saved top 100 sentences to JSON file")