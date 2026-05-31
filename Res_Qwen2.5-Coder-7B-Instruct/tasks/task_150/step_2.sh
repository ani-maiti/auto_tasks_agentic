#!/bin/bash

# Get the list of Python files
py_files=$(cat py_files.txt)

# Initialize an empty dictionary to store file sizes
declare -A file_sizes

# Loop through each Python file and get its size
for file in $py_files; do
    size=$(stat -c%s "$file")
    file_sizes["$file"]=$size
done

# Convert the dictionary to a JSON object
json_output=$(printf "%s\n" "${!file_sizes[@]}" | jq --argjson sizes "$(printf "%s\n" "${file_sizes[@]}")" '. as $files | {($files[]): ($sizes[$files[]])}')

# Write the JSON output to a file
echo "$json_output" > python_files_sizes.json