echo "File extension report generated successfully:"
ls -1 | grep -oE '\.[^.]+$' | sort | uniq -c | sort -nr