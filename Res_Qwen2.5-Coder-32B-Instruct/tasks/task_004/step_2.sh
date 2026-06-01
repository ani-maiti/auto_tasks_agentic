echo "Duplicate filenames found:"
find . -type f -printf "%f\n" | sort | uniq -d