# Step 2: Read all text files and extract sentences
sentences = []
for file in text_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Splitting content into sentences based on common sentence delimiters
        sentences.extend(content.split('。'))

print(f"Extracted {len(sentences)} sentences.")