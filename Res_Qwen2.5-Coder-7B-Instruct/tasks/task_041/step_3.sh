echo "grep command failed. Trying alternative approach..."
find . -type f -name "*.txt" -exec grep -oP 'https?://\S+' {} + > urls.txt