echo "Starting search for files containing dates..."
find . -type f -name '*[0-9][0-9][0-9][0-9]*' -o -name '*[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]*'