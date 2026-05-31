echo "Generating a report of the 100 largest files..."
du -ah --max-depth=1 | sort -hr | head -n 100