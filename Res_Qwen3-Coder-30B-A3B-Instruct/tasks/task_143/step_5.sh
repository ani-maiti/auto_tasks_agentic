echo "The ten longest Python files by line count are:"
find . -name "*.py" -type f -exec wc -l {} \; | sort -nr | head -10 | awk '{print $2 ": " $1 " lines"}'