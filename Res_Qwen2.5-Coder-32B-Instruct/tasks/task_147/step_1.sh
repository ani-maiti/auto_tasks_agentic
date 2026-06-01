echo "Starting search for Python files containing TODO comments..."
find . -name "*.py" -exec grep -Hn "TODO" {} \;