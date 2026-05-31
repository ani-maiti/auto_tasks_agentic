# Extract metadata from each archive and store it in a CSV file
for archive in $(cat archives.txt); do
    echo "Processing $archive"
    tar -tf "$archive" >> archive_metadata.csv
done