echo "Extracting code blocks from Markdown files..."
for file in $(find . -type f -name "*.md"); do
    echo "Processing $file"
    grep -oP '```.*?```' "$file" | sed 's/^```//;s/$$//' > "${file}.codeblocks"
done