echo "Starting search for files containing 'data science'"
find . -type f -exec grep -l "data science" {} \;