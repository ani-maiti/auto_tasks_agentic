echo "Starting to list files..."
find . -type f | awk -F. 'NF>1 {print $NF}' > extensions.txt
echo "File listing complete."