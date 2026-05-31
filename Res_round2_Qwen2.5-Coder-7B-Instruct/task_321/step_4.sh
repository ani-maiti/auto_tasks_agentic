# Remove lines that indicate errors from the CSV file
sed '/This does not look like a tar archive/d' archive_metadata.csv > cleaned_archive_metadata.csv