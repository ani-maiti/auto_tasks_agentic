echo "Starting search for duplicate filenames..."
find . -type f -printf "%f\n" | sort | uniq -d