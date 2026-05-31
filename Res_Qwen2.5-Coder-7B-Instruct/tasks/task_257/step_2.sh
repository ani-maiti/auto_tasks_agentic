# Step 2: Compute perceptual hashes for the found image files
for file in $(find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \)); do
    echo "$file"
done