echo "Report of the 100 Largest Files"
echo "================================"
find /home -type f -exec du -b {} \; 2>/dev/null | sort -nr | head -100 | nl