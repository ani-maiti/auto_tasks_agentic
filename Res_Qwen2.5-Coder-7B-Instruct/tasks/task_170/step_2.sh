# Read the list of text files and process each one
while read file; do
    grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$file"
done < text_files.txt