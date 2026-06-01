echo "Found .md files. Counting headings..."
grep -E '^(#{1,6} )' $(find . -name "*.md") | wc -l