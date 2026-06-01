echo "Finding Markdown files and calculating their sizes..."
find . -type f \( -name "*.md" -o -name "*.markdown" \) -exec du -c {} + | grep total$