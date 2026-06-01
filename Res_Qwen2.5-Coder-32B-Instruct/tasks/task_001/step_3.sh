echo "Final list of the 20 largest files:"
find . -type f -exec du -h {} + | sort -rh | head -n 20