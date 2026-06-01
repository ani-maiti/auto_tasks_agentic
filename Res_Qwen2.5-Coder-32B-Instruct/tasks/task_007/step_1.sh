echo "Starting directory search"
find . -type d | awk -F'/' 'NF > max_length {max_length = NF; deepest_dir = $0} END {print deepest_dir}'