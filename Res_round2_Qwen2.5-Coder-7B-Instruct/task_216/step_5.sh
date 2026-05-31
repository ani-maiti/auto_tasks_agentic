# Load the flattened keys into an associative array
declare -A flattened_keys
while IFS='=' read -r key value; do
    flattened_keys["$key"]=$((flattened_keys["$key"] + 1))
done < flattened_keys.json