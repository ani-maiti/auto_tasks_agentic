echo "Collecting function definitions..."
grep -oP '(?<=def\s)\w+' *.py **/*.py > functions.txt