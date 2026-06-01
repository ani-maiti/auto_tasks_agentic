echo "Starting search for Python files containing FIXME comments."
find . -type f -name "*.py" -exec grep -H "FIXME" {} +