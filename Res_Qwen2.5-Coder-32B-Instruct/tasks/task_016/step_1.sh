echo "Starting file extension count report generation."
ls -1 | grep -oE '\.[^.]+$' | sort | uniq -c | sort -nr
echo "Report generation complete."