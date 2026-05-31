# Correct the syntax error by removing the extra backtick
find . -type f -exec ls -lh {} + | sort -k5 -hr | head -n 101 > largest_files.txt