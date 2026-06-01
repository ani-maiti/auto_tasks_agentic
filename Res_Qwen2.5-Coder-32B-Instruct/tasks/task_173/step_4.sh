echo "Files containing 'machine learning' without false positives:"
grep -Hn "machine learning" $(find . -type f) | grep -v "grep -l" | grep -v "find all files containing the phrase machine learning"