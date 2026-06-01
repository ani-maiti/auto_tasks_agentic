echo "Searching for JSON objects in non-json files..."
grep -r --include=\*.{log,txt} '"[^"]*":' .