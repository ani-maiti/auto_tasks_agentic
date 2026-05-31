# Check if there are any text files in the current directory
if [ ! -f "text_files.txt" ]; then
    echo "No text files found in the current directory."
else
    # Process each text file to extract IPv4 addresses
    while read file; do
        grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$file"
    done < text_files.txt
fi