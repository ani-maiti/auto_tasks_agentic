echo "Saving report to directory_size_report.txt"
du -sh */ 2>/dev/null | sort -rh > directory_size_report.txt