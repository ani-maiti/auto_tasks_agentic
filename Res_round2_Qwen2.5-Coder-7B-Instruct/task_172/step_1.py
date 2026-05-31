import os
import re

# Define a regular expression pattern for URLs
url_pattern = re.compile(r'https?://[^\s]+')

# Walk through the current directory and its subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    urls = url_pattern.findall(content)
                    if urls:
                        print(f"URLs found in {file_path}:")
                        for url in urls:
                            print(url)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
```

This script will walk through the current directory and its subdirectories, looking for text files (`*.txt`). For each text file, it reads the content and extracts URLs using a regular expression pattern. If any URLs are found, it prints them along with the file path.