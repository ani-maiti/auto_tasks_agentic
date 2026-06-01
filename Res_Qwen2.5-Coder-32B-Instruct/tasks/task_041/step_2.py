import re
import os

url_pattern = re.compile(r'https?://[^\s]+')
urls = []

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    found_urls = url_pattern.findall(content)
                    urls.extend(found_urls)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

print("Extracted URLs:")
for url in urls:
    print(url)