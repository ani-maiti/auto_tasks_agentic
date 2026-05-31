# Step 2: Extract outbound URLs from Markdown files
urls = set()
for file in markdown_files:
    with open(file, 'r') as f:
        content = f.read()
        url_pattern = r'https?://[^\s]+'
        urls.update(re.findall(url_pattern, content))

print(f"Extracted {len(urls)} unique URLs.")