echo "Extracting import statements from Python files"
grep -oP 'import \K[a-zA-Z0-9._]+' $(cat python_files.txt) > imports.txt
grep -oP 'from \K[a-zA-Z0-9._]+' $(cat python_files.txt) >> imports.txt
echo "Imports extracted to imports.txt"
cat imports.txt