with open('markdown_files.txt', 'r') as f:
    markdown_files = f.read().splitlines()

print(f"Found {len(markdown_files)} Markdown files.")