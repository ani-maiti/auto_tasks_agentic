echo "Step 2: Count the number of unique words across all text files."
cat $(find . -type f -name "*.txt") | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | sort | uniq | wc -l