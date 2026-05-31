#!/bin/bash

# List all files in the current directory
files=$(ls)

# Initialize an empty array to store results
declare -A results

# Loop through each file
for file in $files; do
  # Check if the file is an archive
  if [[ $file == *.zip ]] || [[ $file == *.tar.gz ]] || [[ $file == *.rar ]]; then
    # Extract the list of files in the archive
    if [[ $file == *.zip ]]; then
      content=$(unzip -l "$file" | awk 'NR>3 {print $4}')
    elif [[ $file == *.tar.gz ]]; then
      content=$(tar -tzf "$file" | awk '{print $NF}')
    elif [[ $file == *.rar ]]; then
      content=$(unrar l "$file" | tail -n +6 | awk '{print $8}')
    fi

    # Find the largest file in the archive
    largest_file=""
    largest_size=0
    for item in $content; do
      size=$(stat -c%s "$item")
      if (( size > largest_size )); then
        largest_file=$item
        largest_size=$size
      fi
    done

    # Store the result
    results["$file"]=$largest_file
  fi
done

# Save the results to a CSV file
echo "Archive,LargestFile" > largest_files.csv
for key in "${!results[@]}"; do
  echo "$key,${results[$key]}" >> largest_files.csv
done

echo "Results saved to largest_files.csv"