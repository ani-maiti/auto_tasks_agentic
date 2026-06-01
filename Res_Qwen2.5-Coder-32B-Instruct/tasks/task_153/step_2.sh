echo "Counting extensions..."
sort extensions.txt | uniq -c | sort -nr > extension_counts.txt
echo "Extension counting complete."