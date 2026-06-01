echo "Starting search for Python files containing the word 'requests'."
find . -name "*.py" -exec grep -l "requests" {} +