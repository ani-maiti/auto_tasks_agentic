import os

markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]
print(markdown_files)