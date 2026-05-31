#!/bin/bash

# Install jq if it's not already installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found. Installing..."
    sudo apt-get update
    sudo apt-get install -y jq
fi

# Continue with the previous script
py_files=$(cat py_files.txt)

declare -A file_sizes

for file in $py_files; do
    size=$(stat -c%s "$file")
    file_sizes["$file"]=$size
done

json_output=$(printf "%s\n" "${!file_sizes[@]}" | jq --argjson sizes "$(printf "%s\n" "${file_sizes[@]}")" '. as $files | {($files[]): ($sizes[$files[]])}')

echo "$json_output" > python_files_sizes.json