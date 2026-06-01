echo "Finding files larger than 1MB..."
find . -type f -size +1M > large_files.txt
echo "Files found. Preparing CSV report..."
awk '{print $5 "," $9}' large_files.txt > report.csv
echo "CSV report generated as report.csv"