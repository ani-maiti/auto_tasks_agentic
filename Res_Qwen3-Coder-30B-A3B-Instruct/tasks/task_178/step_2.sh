echo "Directory Size Report"
echo "====================="
find . -type d -exec du -h {} \; | sort -hr | head -20