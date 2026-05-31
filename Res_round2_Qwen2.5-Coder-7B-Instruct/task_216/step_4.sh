# Loop through each JSON file
for json_file in "${json_files[@]}"; do
    # Use jq to flatten the JSON and add it to the dictionary
    jq 'paths | join(".") as $path | {($path): getpath($path)}' "$json_file" | jq -s '. * .[]' | jq --argfile data "$json_file" '. as $data | ($data | split(".")[:-1] | join(".")) as $key | ($data | split(".")[-1]) as $value | $key + "." + $value' | jq --slurp . | jq -R . | jq -nR '[inputs|split("=")] | from_entries' >> flattened_keys.json
done