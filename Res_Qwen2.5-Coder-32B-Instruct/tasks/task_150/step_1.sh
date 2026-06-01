echo "Starting the process to list all Python files and their sizes."
find . -type f -name "*.py" -exec ls -lh {} \;