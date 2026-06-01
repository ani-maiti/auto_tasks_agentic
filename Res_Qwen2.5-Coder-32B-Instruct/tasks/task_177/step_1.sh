echo "Starting to find the 100 largest files..."
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 100 > largest_files_report.txt
echo "Report generated: largest_files_report.txt"