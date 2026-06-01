echo "Saving report to file_extension_report.txt"
ls -1 | grep -oE '\.[^.]+$' | sort | uniq -c | sort -nr > file_extension_report.txt
echo "Report saved."