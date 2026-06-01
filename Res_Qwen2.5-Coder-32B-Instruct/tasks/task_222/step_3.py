from collections import defaultdict

paragraphs = defaultdict(list)

def read_paragraphs(filename):
    with open(filename, 'r') as file:
        content = file.read()
        para_list = content.split('\n\n')
        for i, paragraph in enumerate(para_list):
            paragraphs[paragraph.strip()].append((filename, i + 1))

for file in text_files:
    read_paragraphs(file)

duplicates = {para: files for para, files in paragraphs.items() if len(files) > 1}

print("Duplicate Paragraphs Report:")
for para, files in duplicates.items():
    print(f"Paragraph found in {len(files)} files:")
    for filename, line in files:
        print(f"  File: {filename}, Line: {line}")
    print(f"Content:\n{para}\n")

largest_duplicate = max(duplicates, key=lambda x: len(x))
print("Largest Duplicated Block:")
print(largest_duplicate)