echo "Extracting code fences from Markdown files..."
for file in $(find . -type f -name "*.md"); do
    echo "Processing $file"
    grep -oP '(?<=```)[^`]+(?=```)' "$file" | while read -r lang; do
        echo "$lang"
    done
done > code_fences.txt