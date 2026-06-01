echo "Identified one timestamp format. Searching for other formats..."
grep -Eo '\b[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}\b' * | sort | uniq -c