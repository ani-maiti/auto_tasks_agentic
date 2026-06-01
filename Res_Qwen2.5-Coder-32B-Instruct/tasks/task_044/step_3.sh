echo "Identified smallest non-empty file:"
find . -type f ! -empty -exec ls -l {} + | sort -n -k 5 | head -n 1