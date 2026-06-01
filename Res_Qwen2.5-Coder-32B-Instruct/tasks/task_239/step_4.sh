echo "Found potential log files. Checking for timestamps..."
grep -Eo '\b[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\b' * | sort | uniq -c