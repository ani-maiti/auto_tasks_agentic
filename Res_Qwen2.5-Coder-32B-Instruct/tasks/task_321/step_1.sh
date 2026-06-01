echo "Starting archive discovery..."
find . -type f \( -iname "*.zip" -o -iname "*.tar" -o -iname "*.gz" -o -iname "*.bz2" -o -iname "*.rar" \) > archives.txt
echo "Archives found:"
cat archives.txt