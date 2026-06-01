echo "Starting the process to find the 100 largest files."
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 100 > largest_files.txt
echo "Finished finding the 100 largest files. Saved to largest_files.txt"