echo "Starting search for files containing 'machine learning'..."
find . -type f -exec grep -l "machine learning" {} \;