echo "Checking for nested Python files in subdirectories..."
find . -type d -exec find {} -type f -name "*.py" \;