#!/bin/bash

# Check if jq is installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found. Installing..."
    # Attempt to install jq using different package managers
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y jq
    elif command -v yum &> /dev/null; then
        sudo yum install -y epel-release
        sudo yum install -y jq
    elif command -v brew &> /dev/null; then
        brew install jq
    else
        echo "Failed to install jq. Please install it manually."
        exit 1
    fi
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