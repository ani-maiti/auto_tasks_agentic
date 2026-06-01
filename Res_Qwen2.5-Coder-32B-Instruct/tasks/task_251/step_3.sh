echo "Collecting function definitions..."
grep -oP '(?<=def\s)\w+' $(find . -name "*.py") > functions.txt