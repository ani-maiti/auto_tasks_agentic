# Step 1: Discover all text files in the current directory and its subdirectories
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

print(f"Found {len(text_files)} text files.")

# Step 2: Read all text files and extract sentences
sentences = {}
for file in text_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Split content into sentences using common delimiters
        sentence_list = content.split('.')
        for sentence in sentence_list:
            if sentence.strip():
                if sentence in sentences:
                    sentences[sentence].append(file)
                else:
                    sentences[sentence] = [file]

print(f"Extracted {len(sentences)} unique sentences.")