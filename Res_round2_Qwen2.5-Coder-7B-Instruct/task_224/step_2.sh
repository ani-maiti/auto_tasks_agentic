# Step 2: Extract metadata for each image
for file in $(find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \)); do
    echo "Extracting metadata for $file"
    exiftool "$file"
done > metadata.txt