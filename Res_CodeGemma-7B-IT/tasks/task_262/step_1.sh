# Find all shell scripts in the current directory
find . -type f -name "*.sh" -print0 | while IFS= read -r -d $'\0' filename; do

  # Extract the filename without the extension
  filename_noext="${filename%.*}"

  # Run the script and capture stdout and stderr
  output=$(./"$filename" 2>&1)

  # Count the number of lines in the script
  script_length=$(wc -l < "$filename")

  # Count the number of external commands used
  command_count=$(grep -Eo '^\s*[a-zA-Z0-9_]+\b' "$filename" | wc -l)

  # Calculate the command frequency
  command_frequency=$(( command_count / script_length * 100 ))

  # Print the report for this script
  echo "## $filename_noext"
  echo "---------------------"
  echo "Lines of code: $script_length"
  echo "External commands: $command_count ($command_frequency%)"
  echo "---------------------"
  echo "$output"

done