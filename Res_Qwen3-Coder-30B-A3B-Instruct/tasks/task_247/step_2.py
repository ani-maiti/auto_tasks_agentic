import os
import re
from collections import defaultdict

# Function to calculate Flesch Reading Ease score
def flesch_reading_ease(text):
    # Count sentences
    sentences = len(re.split(r'[.!?]+', text)) - 1  # Subtract 1 for empty string at end
    
    # Count words
    words = len(text.split())
    
    # Count syllables
    def count_syllables(word):
        word = re.sub(r'[^a-zA-Z]', '', word.lower())
        if not word:
            return 0
        vowels = "aeiouy"
        syllable_count = 0
        if word[0] in vowels:
            syllable_count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                syllable_count += 1
        if word.endswith("e"):
            syllable_count -= 1
        if syllable_count == 0:
            syllable_count = 1
        return syllable_count
    
    syllables = sum(count_syllables(word) for word in text.split())
    
    if sentences == 0 or words == 0:
        return 0
    
    # Calculate Flesch Reading Ease
    FRE = 206.835 - (1.015 * (words / sentences)) - (84.6 * (syllables / words))
    return FRE

# Find all text files
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

# Process each file
readability_scores = []

for file_path in text_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        score = flesch_reading_ease(content)
        readability_scores.append((file_path, score))
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Sort by readability score (higher is easier to read)
readability_scores.sort(key=lambda x: x[1], reverse=True)

# Save report
with open('readability_report.txt', 'w') as f:
    f.write("Readability Report\n")
    f.write("==================\n\n")
    for file_path, score in readability_scores:
        f.write(f"{file_path}: {score:.2f}\n")

# Print the easiest file to read
if readability_scores:
    easiest_file = readability_scores[0][0]
    print(easiest_file)
else:
    print("No text files found.")