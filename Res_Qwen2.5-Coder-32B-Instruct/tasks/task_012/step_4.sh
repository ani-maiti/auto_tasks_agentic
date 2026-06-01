echo "Search complete. Files containing the word TODO:"
grep -rl "TODO" . --exclude=*.log --exclude=*.txt