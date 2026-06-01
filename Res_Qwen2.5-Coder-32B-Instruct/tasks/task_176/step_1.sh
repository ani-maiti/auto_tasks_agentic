echo "Starting file extension frequency report generation."
find . -type f | awk -F. 'NF>1 {print $NF}' | sort | uniq -c | sort -nr > file_extension_report.txt
echo "Report generated and saved to file_extension_report.txt"