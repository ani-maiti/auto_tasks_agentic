echo "Searching for files containing the word TODO excluding log files"
grep -r "TODO" . --exclude=*.log --exclude=*.txt