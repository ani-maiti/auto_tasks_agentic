echo "Checking for URLs in all text files again with grep, excluding problematic files."
grep -oE 'https?://[^\s]+' *.txt */*.txt */*/*.txt */*/*/*.txt 2>/dev/null