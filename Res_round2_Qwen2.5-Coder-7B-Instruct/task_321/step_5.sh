# Identify files that appear in multiple archives
sort cleaned_archive_metadata.csv | uniq -d > duplicate_files.txt