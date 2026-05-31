# Initialize an empty dictionary to store function signatures
declare -A func_signatures

# Loop through each Python file
for file in "${py_files[@]}"; do
    # Extract function names and their signatures
    grep -oP 'def \K[^\(]+' "$file" | while read func_name; do
        func_sig=$(grep -oP "(?<=^$func_name\().*(?=\))" "$file")
        func_signatures["$func_name:$func_sig"]="$file"
    done
done