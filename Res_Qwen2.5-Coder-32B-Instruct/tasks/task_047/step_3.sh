echo "Checking non-json files for JSON objects..."
grep -r --include=\*.{log,json} '"[^"]*":' .