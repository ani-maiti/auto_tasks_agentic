echo "Step 2: Extract words from each text file and store them in a list."
cat $(find . -type f -name "*.txt") | tr '[:space:]' '\n' | grep -oE '[a-zA-Z]+' > words.txt