# Step 2: Read all text files and extract sentences
sentences = {}
for file in text_files:
    try:
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
    except Exception as e:
        print(f"Error reading file {file}: {e}")

print(f"Extracted {len(sentences)} unique sentences.")