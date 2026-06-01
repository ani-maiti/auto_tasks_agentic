echo "Checking for URLs in all text files again with grep."
grep -oE 'https?://[^\s]+' *.txt */*.txt */*/*.txt */*/*/*.txt */*/*/*/*.txt